import torch
import torch.nn.functional as F
import numpy as np


# --- 模拟 nvfp4 核心函数 ---

def quantize_e2m1(tensor):
    """
    模拟 E2M1 量化。E2M1 有1个符号位, 2个指数位, 1个尾数位。
    它能表示的值非常有限，主要包括 +/- 0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0 。
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
    tensor = torch.clamp(tensor, min=2e-3, max=448.0)
    
    # 模拟精度损失：将其量化到一定的步长
    # 这里的步长模拟是近似的，关键是限制其精度
    # 对于一个给定的指数，有8个线性间隔的尾数值
    exponent = torch.floor(torch.log2(tensor + 1e-9))
    mantissa_val = tensor / (2**exponent) - 1.0 # 范围 [0, 1)
    
    # 量化尾数到3位精度 (8个级别)
    quantized_mantissa_val = torch.round(mantissa_val * 8) / 8
    
    # 重构
    reconstructed_val = (1 + quantized_mantissa_val) * (2**exponent)
    return reconstructed_val

def dequantize_ue4m3(tensor):
    # 伪量化中，直接返回模拟后的浮点数值
    return tensor

def quantize_ue8m0(tensor):
    
    exponent = torch.ceil(torch.log2(tensor + 1e-9))
    exponent = max(-127, min(127, exponent))
    
    reconstructed_val = (2**exponent)
    return reconstructed_val

def dequantize_ue8m0(tensor):
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

def quantize_mxfp4_tensor(tensor, group_size=32):

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
    
    # 3. 量化 scale 到 ue8m0
    quantized_scale = quantize_ue8m0(scale)
    dequantized_scale = dequantize_ue8m0(quantized_scale)
    
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

def reorder_quantize_w(w, reorder_index, select_num):
    scale_w = w.abs().max(dim=1, keepdim=True)[0] / 63.0
    scale_w[scale_w == 0] = 1e-9
    scale_w[scale_w != 0] = 1.0
    scaled_w = w / scale_w
    if select_num == 0:
        return quantize_nvfp4_tensor(scaled_w), scale_w
        # return quantize_mxfp4_tensor(scaled_w), scale_w
    else:
        topk_index = reorder_index[:select_num]
        return torch.cat([quantize_nvfp4_tensor(scaled_w), quantize_nvfp4_tensor(scaled_w[:, topk_index])], dim=1), scale_w
        # return torch.cat([quantize_mxfp4_tensor(scaled_w), quantize_mxfp4_tensor(scaled_w[:, topk_index])], dim=1), scale_w

def reorder_quantize_x(x, reorder_index, select_num):
    scale_x = x.abs().max(dim=1, keepdim=True)[0] / 63.0
    scale_x[scale_x == 0] = 1e-9
    scale_x[scale_x != 0] = 1.0
    scaled_x = x / scale_x
    if select_num == 0:
        return quantize_nvfp4_tensor(scaled_x), scale_x
        # return quantize_mxfp4_tensor(scaled_x), scale_x
    else:
        topk_index = reorder_index[:select_num]
        q_x = quantize_nvfp4_tensor(scaled_x)
        # q_x = quantize_mxfp4_tensor(scaled_x)
        error_e = scaled_x - q_x
        q_error_k = quantize_nvfp4_tensor(error_e[:, topk_index])
        # q_error_k = quantize_mxfp4_tensor(error_e[:, topk_index])
        return torch.cat([q_x, q_error_k], dim=1), scale_x
