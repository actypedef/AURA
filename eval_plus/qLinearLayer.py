import torch
import torch.nn as nn

import sys
sys.path.append('kernels/build/')
import agemm

import math
import random

def find_qlinear_layers(module, name=''):
    if type(module) == QLinearLayer:
        if module.enable_quant:
            return {name: module}
    res = {}
    for name1, child in module.named_children():
        res.update(find_qlinear_layers(
            child, name=name + '.' + name1 if name != '' else name1
        ))
    return res
    
class QLinearLayer(nn.Module):
    def __init__(
        self,
        originalLayer: nn.Linear,
        select_num, 
        reorder_index,
        out_reorder_index=None,
    ):
        super().__init__()
      
        self.in_features = originalLayer.in_features
        self.out_features = originalLayer.out_features
    
        
        if originalLayer.bias is not None:
            self.register_buffer('bias', originalLayer.bias)
        else:
            self.bias = None
        
        self.select_num = select_num
        # if out_reorder_index is not None:
        #     self.weight = torch.index_select(originalLayer.weight.data, 0, out_reorder_index)
        self.W, self.scale_w = agemm.reorder_quantize_w(originalLayer.weight.data, reorder_index.to(torch.int16).cuda(), select_num)
        
        
        reorder_index.cpu()
        del reorder_index
        torch.cuda.empty_cache()

    @torch.no_grad()
    def forward(self, x):
        qx, scale_x, bsz, q_len = x
        
        y = agemm.matmul(qx, self.W, scale_x, self.scale_w)
        if self.bias is not None:
            y = y + self.bias

        y = y.reshape(bsz, q_len, -1)
        return y
    