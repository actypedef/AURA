import torch
import torch.nn.functional as F
import numpy as np

# --- 模拟 nvfp4 核心函数 ---

def quantize_e2m1(tensor):
    """
    模拟 E2M1 量化。E2M1 有1个符号位, 2个指数位, 1个尾数位。
    它能表示的值非常有限，主要包括 +/- 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0 以及 NaN/Inf。
    为了简化模拟，我们直接定义这些可表示的值，然后找最近的。
    """
    # E2M1 可表示的有限数值集合 (不包括 NaN/Inf)
    representable_vals = torch.tensor([
        -6.0, -4.0, -3.0, -2.0, -1.5, -1.0, -0.5, 0.0,
        0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0
    ], device=tensor.device, dtype=tensor.dtype)
    
    # 使用广播和argmin找到每个元素最近的可表示值
    diff = torch.abs(tensor.unsqueeze(-1) - representable_vals)
    indices = torch.argmin(diff, dim=-1)
    return representable_vals[indices]

def dequantize_e2m1(tensor):
    # 在伪量化中，已经是模拟后的浮点数值，直接返回
    return tensor

def quantize_ue4m3(tensor):
    """
    模拟 UE4M3 (Unsigned E4M3) 量化。
    这是一个无符号格式，常用于缩放因子。
    我们将通过限制其最大值和精度来模拟。
    E4M3 的最大值是 448.
    """
    # 裁剪到UE4M3可表示的范围 [0, 448]
    tensor = torch.clamp(tensor, min=1/512, max=448.0)
    
    # 模拟精度损失：将其量化到一定的步长
    # 这里的步长模拟是近似的，关键是限制其精度
    # 对于一个给定的指数，有8个线性间隔的尾数值
    exponent = torch.floor(torch.log2(tensor))
    mantissa_val = tensor / (2**exponent) - 1.0 # 范围 [0, 1)
    
    # 量化尾数到3位精度 (8个级别)
    quantized_mantissa_val = torch.round(mantissa_val * 8) / 8
    
    # 重构
    reconstructed_val = (1 + quantized_mantissa_val) * (2**exponent)
    return reconstructed_val

def dequantize_ue4m3(tensor):
    # 伪量化中，直接返回模拟后的浮点数值
    return tensor

def quantize_nvfp4_tensor(tensor, group_size=16):
    """
    对一个张量进行完整的 nvfp4 伪量化。
    1. 分组
    2. 为每组找到最佳缩放因子 (scale)
    3. 量化 scale 到 ue4m3
    4. 使用 scale 归一化组内数据
    5. 量化归一化后的数据到 e2m1
    """
    original_shape = tensor.shape
    
    # 填充张量以确保其最后一个维度是 group_size 的倍数
    padding = (group_size - tensor.shape[-1] % group_size) % group_size
    if padding != 0:
        tensor = F.pad(tensor, (0, padding))
        
    reshaped_tensor = tensor.view(-1, group_size)
    
    # 2. 计算缩放因子 (scale)
    # 目标是让组内数据缩放到 E2M1 的有效范围内，比如 [-6, 6]
    # 我们选择组内绝对值的最大值，然后除以 E2M1 的最大值 6.0
    max_abs_val = torch.max(torch.abs(reshaped_tensor), dim=1, keepdim=True)[0]
    scale = max_abs_val / 6.0
    scale[scale == 0] = 1e-9 # 避免除以零
    
    # 3. 量化 scale 到 ue4m3
    quantized_scale = quantize_ue4m3(scale)
    dequantized_scale = dequantize_ue4m3(quantized_scale)
    
    # 4. 归一化数据
    normalized_tensor = reshaped_tensor / dequantized_scale
    
    # 5. 量化到 e2m1
    quantized_e2m1_tensor = quantize_e2m1(normalized_tensor)
    
    # --- 反量化以模拟精度损失 ---
    dequantized_tensor_groups = dequantize_e2m1(quantized_e2m1_tensor) * dequantized_scale
    
    # 恢复形状
    dequantized_tensor = dequantized_tensor_groups.view(tensor.shape)
    
    # 移除填充
    if padding != 0:
        dequantized_tensor = dequantized_tensor[..., :-padding]
        
    return dequantized_tensor.view(original_shape)

class Quantizer:
    """量化器抽象基类"""
    def __init__(self, **kwargs):
        pass

    def quantize_linear_layer(self, x, w):
        """
        对一个线性层 X * W^T 进行量化和计算。
        返回伪量化计算后的输出 Y。
        """
        raise NotImplementedError

    def get_name(self):
        return self.__class__.__name__

class FP32Baseline(Quantizer):
    """全精度基线，不进行任何量化"""
    def quantize_linear_layer(self, x, w):
        return F.linear(x, w)

# --- 你的量化方法实现 ---
class Nvfp4AugmentedQuantizer(Quantizer):
    def __init__(self, k, group_size=16):
        """
        k: 要补偿的关键通道数量。k=0表示不进行补偿。
        group_size: nvfp4 的组大小。
        """
        super().__init__()
        # **修改点 1: 允许k=0**
        assert k >= 0, "k必须为非负整数"
        self.k = k
        self.group_size = group_size

    def get_name(self):
        if self.k == 0:
            return "Nvfp4Base"
        return f"Nvfp4Augmented(k={self.k})"

    def quantize_linear_layer(self, x, w):
        # --- 1. 计算二级 (per-token) 缩放因子 (对所有k值通用) ---
        scale_x = x.abs().max(dim=1, keepdim=True)[0] / 63.0
        scale_x = torch.ones(scale_x.shape, dtype=torch.bfloat16, device='cuda')
        scale_x[scale_x == 0] = 1e-9
        scale_w = w.abs().max(dim=1, keepdim=True)[0] / 63.0
        scale_w = torch.ones(scale_w.shape, dtype=torch.bfloat16, device='cuda')
        scale_w[scale_w == 0] = 1e-9
        
        x_scaled = x / scale_x
        w_scaled = w / scale_w

        # **修改点 2: 根据 k 的值选择不同逻辑分支**
        if self.k > 0:
            # --- 分支 A: k > 0, 执行误差补偿和矩阵增广 ---

            # 2. 关键通道选择
            q_x_trial = quantize_nvfp4_tensor(x_scaled, self.group_size)
            error_e = x_scaled - q_x_trial
            norm_e = torch.linalg.norm(error_e, ord=2, dim=0)
            norm_w = torch.linalg.norm(w_scaled, ord=2, dim=0)
            importance_scores = norm_e * norm_w
            _, top_k_indices = torch.topk(importance_scores, self.k)
            
            # 3. 构建增广矩阵
            q_x = quantize_nvfp4_tensor(x_scaled, self.group_size)
            q_w = quantize_nvfp4_tensor(w_scaled, self.group_size)
            
            error_k = error_e[:, top_k_indices]
            q_error_k = quantize_nvfp4_tensor(error_k, self.group_size)
            
            w_k = w_scaled[:, top_k_indices]
            # 权重补偿部分直接复制，而不是量化其误差
            q_w_k = quantize_nvfp4_tensor(w_k, self.group_size)

            x_gemm = torch.cat([q_x, q_error_k], dim=1)
            w_gemm = torch.cat([q_w, q_w_k], dim=1)

        else: # self.k == 0
            # --- 分支 B: k = 0, 只进行基础的nvfp4量化 ---
            q_x = quantize_nvfp4_tensor(x_scaled, self.group_size)
            q_w = quantize_nvfp4_tensor(w_scaled, self.group_size)
            
            x_gemm = q_x
            w_gemm = q_w

        # --- 4. 矩阵乘法 (对所有k值通用) ---
        y_quantized_scaled = F.linear(x_gemm, w_gemm)

        # --- 5. 二级 (per-token) 反量化 (对所有k值通用) ---
        final_scale = scale_x @ scale_w.T
        y_final = y_quantized_scaled * final_scale
        
        return y_final

# --- 对比方法：INT8 和 W4A16 ---
class INT8Quantizer(Quantizer):
    def quantize_linear_layer(self, x, w):
        # Per-tensor对称量化
        scale_x = x.abs().max() / 127.0
        scale_w = w.abs().max() / 127.0
        
        q_x = torch.round(x / scale_x).clamp(-128, 127)
        q_w = torch.round(w / scale_w).clamp(-128, 127)
        
        # 反量化以模拟精度损失
        dq_x = q_x * scale_x
        dq_w = q_w * scale_w
        
        return F.linear(dq_x, dq_w)

class W4A16Quantizer(Quantizer):
    def quantize_linear_layer(self, x, w):
        # A16: Activations (x) 使用 FP16 或 BF16，这里用 FP16 模拟
        x_a16 = x.to(torch.float16).to(torch.float32) # 模拟精度损失
        
        # W4: Weights (w) 进行4-bit量化
        # Per-channel 对称量化
        scale_w = w.abs().max(dim=1, keepdim=True)[0] / 7.0 # 4-bit range [-8, 7]
        scale_w[scale_w == 0] = 1e-9
        
        q_w = torch.round(w / scale_w).clamp(-8, 7)
        dq_w = q_w * scale_w
        
        return F.linear(x_a16, dq_w)

class INT4Quantizer(Quantizer):
    def quantize_linear_layer(self, x, w):
        # Per-tensor对称量化
        scale_x = x.abs().max() / 7.0
        scale_w = w.abs().max() / 7.0
        
        q_x = torch.round(x / scale_x).clamp(-8, 7)
        q_w = torch.round(w / scale_w).clamp(-8, 7)
        
        # 反量化以模拟精度损失
        dq_x = q_x * scale_x
        dq_w = q_w * scale_w
        
        return F.linear(dq_x, dq_w)

def run_experiment(seq_len=128, in_features=512, out_features=1024):
    """运行量化实验并打印结果"""
    print(f"\n--- Running Experiment ---")
    print(f"Matrix shapes: X({seq_len}, {in_features}), W({out_features}, {in_features})")

    # --- 1. 生成数据 ---
    M, N, K = seq_len, out_features, in_features
    w = torch.rand(N, K, dtype=torch.bfloat16, device='cuda') * 3
    # w = torch.eye(K, dtype=torch.bfloat16, device='cuda')
    
    KN, KS, KO = 4096-512, 512-128, 128
    signs = (torch.randint(0, 2, (M, K), dtype=torch.bfloat16, device='cuda') * 2 - 1)
    x = torch.rand(M, K, dtype=torch.bfloat16, device='cuda') * 3
    x[:, -KS:] = torch.rand(M, KS, dtype=torch.bfloat16, device='cuda') * 3 + 3
    x[:, -KO:] = torch.rand(M, KO, dtype=torch.bfloat16, device='cuda') * 8 + 8
    x[:, -16:] = torch.rand(M, 16, dtype=torch.bfloat16, device='cuda') * 16 + 16
    x = x * signs
    
    # --- 2. 定义量化器列表 ---
    quantizers = [
        FP32Baseline(),
        # INT8Quantizer(),
        # W4A16Quantizer(),
        # INT4Quantizer(),
        Nvfp4AugmentedQuantizer(k=0),
        Nvfp4AugmentedQuantizer(k=512),
        Nvfp4AugmentedQuantizer(k=1024),
        Nvfp4AugmentedQuantizer(k=1536),
        Nvfp4AugmentedQuantizer(k=2048),
        Nvfp4AugmentedQuantizer(k=2560),
        Nvfp4AugmentedQuantizer(k=3072),
        Nvfp4AugmentedQuantizer(k=3584),
        Nvfp4AugmentedQuantizer(k=4096),
    ]
    
    # --- 3. 运行并评估 ---
    # 计算FP32基准结果
    y_true = quantizers[0].quantize_linear_layer(x, w)
    
    print("\n--- MSE Analysis ---")
    print(f"{'Quantization Method':<25} | {'MSE':<15}")
    print("-" * 45)

    for quantizer in quantizers[1:]: # 跳过FP32本身
        # 得到量化后的输出
        y_quant = quantizer.quantize_linear_layer(x, w)
        
        # 计算MSE
        mse = F.mse_loss(y_true, y_quant).item()
        
        print(f"{quantizer.get_name():<25} | {mse:<15.8e}")

if __name__ == '__main__':
    # 为了结果可复现，设置随机种子
    torch.manual_seed(45510)
    
    run_experiment(seq_len=1, in_features=4096, out_features=4096)