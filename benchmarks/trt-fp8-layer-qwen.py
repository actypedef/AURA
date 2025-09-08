import tensorrt as trt
import torch
import numpy as np
import time
import traceback

# 1. 定义 Qwen2.5-7B 解码器层的结构参数


# TensorRT 日志记录器
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

import tensorrt as trt
import torch
import numpy as np
import time
import traceback

# 1. 定义 Qwen2.5-7B 解码器层的结构参数（测速用）
BATCH_SIZE = 1
SEQ_LEN = 64
HIDDEN_SIZE = 5120
NUM_ATTENTION_HEADS = 40
NUM_KV_HEADS = 8
HEAD_DIM = HIDDEN_SIZE // NUM_ATTENTION_HEADS
FFN_HIDDEN_SIZE = 13824
GQA_FACTOR = NUM_ATTENTION_HEADS // NUM_KV_HEADS 

# TensorRT 日志记录器
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

def create_dummy_weights(shape, dtype=np.float16):
    """创建一个包含随机数据的 trt.Weights 对象"""
    return trt.Weights(np.random.rand(*shape).astype(dtype))

def _create_rope_cache(network, dtype):
    """预计算 RoPE 的 sin 和 cos 缓存并作为常量添加到网络中"""
    print("Creating RoPE cache...")
    theta_base = 1000000.0  # Qwen2 使用的 base

    theta = theta_base ** (-2.0 * np.arange(0, HEAD_DIM, 2, dtype=np.float32) / HEAD_DIM)
    position = np.arange(SEQ_LEN, dtype=np.float32)
    freqs = np.outer(position, theta)
    emb = np.concatenate((freqs, freqs), axis=-1)

    cos_cache = np.cos(emb)[np.newaxis, :, np.newaxis, :].astype(dtype)
    sin_cache = np.sin(emb)[np.newaxis, :, np.newaxis, :].astype(dtype)

    # 调整为 [1, 1, seq_len, head_dim] 便于广播
    cos_cache_reshaped = np.transpose(cos_cache, (0, 2, 1, 3))
    sin_cache_reshaped = np.transpose(sin_cache, (0, 2, 1, 3))

    cos_const = network.add_constant(cos_cache_reshaped.shape, trt.Weights(cos_cache_reshaped)).get_output(0)
    sin_const = network.add_constant(sin_cache_reshaped.shape, trt.Weights(sin_cache_reshaped)).get_output(0)
    cos_const.name = "rope_cos_cache"
    sin_const.name = "rope_sin_cache"
    return cos_const, sin_const

def add_rope(network, input_tensor, cos_cache, sin_cache):
    """在网络中添加 RoPE 层"""
    head_dim_half = HEAD_DIM // 2

    # 切片前半部分 [x1]
    slice_shape = list(input_tensor.shape)
    slice_shape[-1] = head_dim_half
    slice_layer1 = network.add_slice(input_tensor, start=[0,0,0,0], shape=slice_shape, stride=[1,1,1,1])
    x1 = slice_layer1.get_output(0)

    # 切片后半部分 [x2]
    slice_layer2 = network.add_slice(input_tensor, start=[0,0,0,head_dim_half], shape=slice_shape, stride=[1,1,1,1])
    x2 = slice_layer2.get_output(0)

    # 构造 [-x2, x1]
    neg_x2 = network.add_unary(x2, trt.UnaryOperation.NEG).get_output(0)
    concat_layer = network.add_concatenation([neg_x2, x1])
    concat_layer.axis = 3
    concat_layer.name = "rope_rotate"
    rotated_input = concat_layer.get_output(0)

    # 应用 RoPE: x * cos + rotate(x) * sin
    cos_term = network.add_elementwise(input_tensor, cos_cache, trt.ElementWiseOperation.PROD).get_output(0)
    sin_term = network.add_elementwise(rotated_input, sin_cache, trt.ElementWiseOperation.PROD).get_output(0)
    output_tensor = network.add_elementwise(cos_term, sin_term, trt.ElementWiseOperation.SUM).get_output(0)
    output_tensor.name = "rope_output"
    return output_tensor

def add_rmsnorm(network, input_tensor, weight_shape):
    """在网络中添加 RMSNorm 层"""
    epsilon = 1e-5
    dtype = np.float16

    pow2_tensor = network.add_elementwise(input_tensor, input_tensor, trt.ElementWiseOperation.PROD).get_output(0)
    
    reduce_axes = 1 << (len(input_tensor.shape) - 1)  # 最后一维
    mean_tensor = network.add_reduce(pow2_tensor, trt.ReduceOperation.AVG, axes=reduce_axes, keep_dims=True).get_output(0)
    
    epsilon_tensor = network.add_constant(shape=(1,) * len(input_tensor.shape), weights=trt.Weights(np.array([epsilon], dtype=dtype))).get_output(0)
    add_eps_tensor = network.add_elementwise(mean_tensor, epsilon_tensor, trt.ElementWiseOperation.SUM).get_output(0)

    sqrt_tensor = network.add_unary(add_eps_tensor, trt.UnaryOperation.SQRT).get_output(0)
    reciprocal_sqrt_tensor = network.add_unary(sqrt_tensor, trt.UnaryOperation.RECIP).get_output(0)
    normalized_tensor = network.add_elementwise(input_tensor, reciprocal_sqrt_tensor, trt.ElementWiseOperation.PROD).get_output(0)

    # 创建可学习权重
    weight_const_1d = network.add_constant(weight_shape, create_dummy_weights(weight_shape, dtype=dtype)).get_output(0)
    shuffle_layer = network.add_shuffle(weight_const_1d)
    reshape_dims = [1] * len(input_tensor.shape)
    reshape_dims[-1] = weight_shape[0]
    shuffle_layer.reshape_dims = tuple(reshape_dims)
    weight_const_reshaped = shuffle_layer.get_output(0)

    output_tensor = network.add_elementwise(normalized_tensor, weight_const_reshaped, trt.ElementWiseOperation.PROD).get_output(0)
    output_tensor.name = "rmsnorm_output"
    return output_tensor

def build_decoder_layer_engine():
    """构建使用 FP8 的 Qwen2.5-7B 解码器层 TensorRT 引擎（用于测速）"""
    builder = trt.Builder(TRT_LOGGER)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.STRONGLY_TYPED))
    config = builder.create_builder_config()

    # ⚠️ 注意：真实部署需校准 scale，此处仅为触发 FP8 融合
    scale_val = 0.1
    scale_tensor = network.add_constant((), trt.Weights(np.array([scale_val], dtype=np.float32))).get_output(0)
    scale_tensor.name = "Global_FP8_Scale"

    def add_fp8_linear_op(input_tensor, weight_tensor, op_type, bias_tensor=None, equation=None, transpose_b=False, op_name=""):
        """
        构造 Q-DQ 模式以触发 TensorRT FP8 融合。
        """
        # 输入量化-反量化
        input_q = network.add_quantize(input_tensor, scale_tensor, trt.DataType.FP8)
        input_q.name = f"{op_name}_input_quant"
        input_dq = network.add_dequantize(input_q.get_output(0), scale_tensor, trt.float16)
        input_dq.name = f"{op_name}_input_dequant"
        dequantized_input = input_dq.get_output(0)

        # 权重量化-反量化
        weight_q = network.add_quantize(weight_tensor, scale_tensor, trt.DataType.FP8)
        weight_q.name = f"{op_name}_weight_quant"
        weight_dq = network.add_dequantize(weight_q.get_output(0), scale_tensor, trt.float16)
        weight_dq.name = f"{op_name}_weight_dequant"
        dequantized_weight = weight_dq.get_output(0)

        # 矩阵乘法
        if op_type == 'einsum':
            layer = network.add_einsum([dequantized_input, dequantized_weight], equation)
        elif op_type == 'matmul':
            op_b = trt.MatrixOperation.TRANSPOSE if transpose_b else trt.MatrixOperation.NONE
            layer = network.add_matrix_multiply(dequantized_input, trt.MatrixOperation.NONE, dequantized_weight, op_b)
        else:
            raise ValueError(f"Unsupported op_type: {op_type}")
        layer.name = op_name
        matmul_output = layer.get_output(0)
        
        # 加偏置（如果提供）
        if bias_tensor is not None:
            bias_add_layer = network.add_elementwise(matmul_output, bias_tensor, trt.ElementWiseOperation.SUM)
            bias_add_layer.name = f"{op_name}_bias_add"
            return bias_add_layer.get_output(0)
            
        return matmul_output

    # --- 构建网络 ---
    input_tensor = network.add_input(name="input_hidden_state", dtype=trt.float16, shape=(BATCH_SIZE, SEQ_LEN, HIDDEN_SIZE))
    
    # Pre-Attention RMSNorm
    normed_input = add_rmsnorm(network, input_tensor, (HIDDEN_SIZE,))
    normed_input.name = "pre_attn_norm_output"

    # ========== Attention ==========
    print("Building Attention Block with FP8 pattern...")

    # 创建带偏置的投影层权重
    q_proj_w = network.add_constant((HIDDEN_SIZE, HIDDEN_SIZE), create_dummy_weights((HIDDEN_SIZE, HIDDEN_SIZE))).get_output(0)
    q_proj_b = network.add_constant((1, 1, HIDDEN_SIZE), create_dummy_weights((1, 1, HIDDEN_SIZE))).get_output(0)
    k_proj_w = network.add_constant((HIDDEN_SIZE, NUM_KV_HEADS * HEAD_DIM), create_dummy_weights((HIDDEN_SIZE, NUM_KV_HEADS * HEAD_DIM))).get_output(0)
    k_proj_b = network.add_constant((1, 1, NUM_KV_HEADS * HEAD_DIM), create_dummy_weights((1, 1, NUM_KV_HEADS * HEAD_DIM))).get_output(0)
    v_proj_w = network.add_constant((HIDDEN_SIZE, NUM_KV_HEADS * HEAD_DIM), create_dummy_weights((HIDDEN_SIZE, NUM_KV_HEADS * HEAD_DIM))).get_output(0)
    v_proj_b = network.add_constant((1, 1, NUM_KV_HEADS * HEAD_DIM), create_dummy_weights((1, 1, NUM_KV_HEADS * HEAD_DIM))).get_output(0)
    o_proj_w = network.add_constant((HIDDEN_SIZE, HIDDEN_SIZE), create_dummy_weights((HIDDEN_SIZE, HIDDEN_SIZE))).get_output(0)
    o_proj_b = network.add_constant((1, 1, HIDDEN_SIZE), create_dummy_weights((1, 1, HIDDEN_SIZE))).get_output(0)

    # 投影
    q_proj = add_fp8_linear_op(normed_input, q_proj_w, 'einsum', bias_tensor=q_proj_b, equation="bsk,kn->bsn", op_name="Q_Proj")
    k_proj = add_fp8_linear_op(normed_input, k_proj_w, 'einsum', bias_tensor=k_proj_b, equation="bsk,kn->bsn", op_name="K_Proj")
    v_proj = add_fp8_linear_op(normed_input, v_proj_w, 'einsum', bias_tensor=v_proj_b, equation="bsk,kn->bsn", op_name="V_Proj")

    # 重塑为多头格式 [B, S, H, D] -> [B, H, S, D]
    def reshape_and_transpose(tensor, num_heads):
        shuffle_layer = network.add_shuffle(tensor)
        shuffle_layer.reshape_dims = (BATCH_SIZE, SEQ_LEN, num_heads, HEAD_DIM)
        shuffle_layer.second_transpose = trt.Permutation([0, 2, 1, 3])  # [B, S, H, D] -> [B, H, S, D]
        shuffle_layer.name = f"reshape_transpose_{num_heads}heads"
        return shuffle_layer.get_output(0)

    q_reshaped = reshape_and_transpose(q_proj, NUM_ATTENTION_HEADS)
    k_reshaped = reshape_and_transpose(k_proj, NUM_KV_HEADS)
    v_reshaped = reshape_and_transpose(v_proj, NUM_KV_HEADS)

    # 应用 RoPE
    cos_cache, sin_cache = _create_rope_cache(network, np.float16)
    q_with_rope = add_rope(network, q_reshaped, cos_cache, sin_cache)
    k_with_rope = add_rope(network, k_reshaped, cos_cache, sin_cache)

    # ✅ 修复：GQA 正确在 axis=1 (num_heads) 上重复
    def repeat_kv(kv_tensor):
        if GQA_FACTOR == 1:
            return kv_tensor
        repeated_list = [kv_tensor] * GQA_FACTOR
        concat_layer = network.add_concatenation(repeated_list)
        concat_layer.axis = 1  # 在 num_heads 维度拼接！
        concat_layer.name = "GQA_KV_Repeat"
        return concat_layer.get_output(0)

    k_repeated = repeat_kv(k_with_rope)
    v_repeated = repeat_kv(v_reshaped)

    # QK^T
    qkT = add_fp8_linear_op(q_with_rope, k_repeated, 'matmul', transpose_b=True, op_name="QKT_MatMul")

    # Scale
    scale_factor = 1.0 / (HEAD_DIM ** 0.5)
    scale_const = network.add_constant((1,1,1,1), trt.Weights(np.array([scale_factor], dtype=np.float16))).get_output(0)
    qkT_scaled = network.add_elementwise(qkT, scale_const, trt.ElementWiseOperation.PROD).get_output(0)
    qkT_scaled.name = "scaled_qkt"

    # Softmax
    softmax_layer = network.add_softmax(qkT_scaled)
    softmax_layer.axes = 1 << 3  # 在最后一个维度（head_dim -> 实际是 seq_len 维度？）
    # 注意：qkT_scaled 形状是 [B, H, S_q, S_k]，应在 S_k 维度（axis=3）做 softmax
    softmax_layer.name = "attention_softmax"
    attention_probs = softmax_layer.get_output(0)

    # Attention 输出
    attn_out_bshd = add_fp8_linear_op(attention_probs, v_repeated, 'matmul', op_name="ProbsV_MatMul")

    # 合并头：[B, H, S, D] -> [B, S, H*D]
    shuffle_out = network.add_shuffle(attn_out_bshd)
    shuffle_out.first_transpose = trt.Permutation([0, 2, 1, 3])  # [B, H, S, D] -> [B, S, H, D]
    shuffle_out.reshape_dims = (BATCH_SIZE, SEQ_LEN, HIDDEN_SIZE)  # 合并最后两维
    shuffle_out.name = "merge_heads"
    attn_out_bsn = shuffle_out.get_output(0)

    # O 投影
    attention_output = add_fp8_linear_op(attn_out_bsn, o_proj_w, 'einsum', bias_tensor=o_proj_b, equation="bsk,kn->bsn", op_name="O_Proj")

    # 第一次残差
    residual1 = network.add_elementwise(input_tensor, attention_output, trt.ElementWiseOperation.SUM).get_output(0)
    residual1.name = "post_attn_residual"

    # Post-FFN Norm
    normed_residual1 = add_rmsnorm(network, residual1, (HIDDEN_SIZE,))
    normed_residual1.name = "post_attn_norm_output"

    # ========== FFN (SwiGLU) ==========
    print("Building FFN Block with FP8 pattern...")

    ffn_gate_w = network.add_constant((HIDDEN_SIZE, FFN_HIDDEN_SIZE), create_dummy_weights((HIDDEN_SIZE, FFN_HIDDEN_SIZE))).get_output(0)
    ffn_gate_b = network.add_constant((1, 1, FFN_HIDDEN_SIZE), create_dummy_weights((1, 1, FFN_HIDDEN_SIZE))).get_output(0)
    ffn_up_w = network.add_constant((HIDDEN_SIZE, FFN_HIDDEN_SIZE), create_dummy_weights((HIDDEN_SIZE, FFN_HIDDEN_SIZE))).get_output(0)
    ffn_up_b = network.add_constant((1, 1, FFN_HIDDEN_SIZE), create_dummy_weights((1, 1, FFN_HIDDEN_SIZE))).get_output(0)
    ffn_down_w = network.add_constant((FFN_HIDDEN_SIZE, HIDDEN_SIZE), create_dummy_weights((FFN_HIDDEN_SIZE, HIDDEN_SIZE))).get_output(0)
    ffn_down_b = network.add_constant((1, 1, HIDDEN_SIZE), create_dummy_weights((1, 1, HIDDEN_SIZE))).get_output(0)

    gate_proj = add_fp8_linear_op(normed_residual1, ffn_gate_w, 'einsum', bias_tensor=ffn_gate_b, equation="bsk,kn->bsn", op_name="FFN_Gate")
    up_proj = add_fp8_linear_op(normed_residual1, ffn_up_w, 'einsum', bias_tensor=ffn_up_b, equation="bsk,kn->bsn", op_name="FFN_Up")

    # SwiGLU: silu(gate) * up
    sigmoid_gate = network.add_activation(gate_proj, trt.ActivationType.SIGMOID).get_output(0)
    silu_out = network.add_elementwise(gate_proj, sigmoid_gate, trt.ElementWiseOperation.PROD).get_output(0)
    silu_out.name = "SiLU_Output"
    gated_ffn = network.add_elementwise(silu_out, up_proj, trt.ElementWiseOperation.PROD).get_output(0)
    gated_ffn.name = "gated_ffn_output"

    # Down Proj
    ffn_output = add_fp8_linear_op(gated_ffn, ffn_down_w, 'einsum', bias_tensor=ffn_down_b, equation="bsk,kn->bsn", op_name="FFN_Down")

    # 最终残差
    final_output = network.add_elementwise(residual1, ffn_output, trt.ElementWiseOperation.SUM).get_output(0)
    final_output.name = "output_hidden_state"
    network.mark_output(final_output)

    # --- 构建引擎 ---
    print("Building TensorRT engine... (This may take a few minutes)")
    plan = builder.build_serialized_network(network, config)
    if not plan:
        print("ERROR: Engine build failed.")
        return None
    
    print("✅ Engine build successful!")
    return plan

def benchmark(engine_plan):
    """使用构建的引擎进行性能测试"""
    runtime = trt.Runtime(TRT_LOGGER)
    engine = runtime.deserialize_cuda_engine(engine_plan)
    context = engine.create_execution_context()

    input_shape = (BATCH_SIZE, SEQ_LEN, HIDDEN_SIZE)
    output_shape = (BATCH_SIZE, SEQ_LEN, HIDDEN_SIZE)
    
    input_tensor = torch.randn(input_shape, dtype=torch.float16, device='cuda')
    output_tensor = torch.empty(output_shape, dtype=torch.float16, device='cuda')
    
    context.set_tensor_address("input_hidden_state", input_tensor.data_ptr())
    context.set_tensor_address("output_hidden_state", output_tensor.data_ptr())

    print("Warming up...")
    warmup_iters = 100  # 原公式太复杂，简化为固定100次
    for _ in range(warmup_iters):
        context.execute_async_v3(stream_handle=torch.cuda.current_stream().cuda_stream)
    torch.cuda.synchronize()
    print("Warm-up finished.")

    num_runs = 500  # 固定500次测速，避免公式复杂化
    start_event = torch.cuda.Event(enable_timing=True)
    end_event = torch.cuda.Event(enable_timing=True)

    print(f"Running benchmark for {num_runs} iterations...")
    start_event.record()
    for _ in range(num_runs):
        context.execute_async_v3(stream_handle=torch.cuda.current_stream().cuda_stream)
    end_event.record()
    torch.cuda.synchronize()

    total_time_ms = start_event.elapsed_time(end_event)
    avg_latency = total_time_ms / num_runs
    tokens_per_run = BATCH_SIZE * SEQ_LEN
    throughput = (tokens_per_run * num_runs) / (total_time_ms / 1000)  # tokens per second

    print("\n" + "="*50)
    print("🚀 BENCHMARK RESULTS")
    print("="*50)
    print(f"Model:          Qwen2.5-7B Decoder Layer (FP8 Simulation)")
    print(f"Batch Size:     {BATCH_SIZE}")
    print(f"Sequence Len:   {SEQ_LEN}")
    print(f"Precision:      FP8 (via Q/DQ Fusion Pattern)")
    print(f"GPU:            {torch.cuda.get_device_name(0)}")
    print("-" * 50)
    print(f"Average Latency:    {avg_latency:.3f} ms")
    print(f"Throughput:         {throughput:,.2f} tokens/sec")
    print("="*50)

if __name__ == "__main__":
    print(f"TensorRT version: {trt.__version__}")
    
    if not torch.cuda.is_available():
        print("❌ ERROR: CUDA is not available.")
        exit(1)
    elif torch.cuda.get_device_properties(0).major < 9:
        print(f"❌ ERROR: FP8 requires compute capability >= 9.0 (Hopper).")
        print(f"Your GPU: {torch.cuda.get_device_name(0)} (CC {torch.cuda.get_device_properties(0).major}.{torch.cuda.get_device_properties(0).minor})")
        exit(1)
    else:
        print(f"✅ GPU: {torch.cuda.get_device_name(0)} (CC {torch.cuda.get_device_properties(0).major}.{torch.cuda.get_device_properties(0).minor})")

    try:
        print("\n🔧 Building Engine...")
        engine_plan = build_decoder_layer_engine()
        if engine_plan:
            print("\n⏱️  Starting Benchmark...")
            benchmark(engine_plan)
        else:
            print("❌ Failed to build engine.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        traceback.print_exc()