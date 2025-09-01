from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, LlamaForCausalLM, Qwen2ForCausalLM
from datasets import load_dataset
import torch.nn as nn
import gc
import torch
from collections import defaultdict
import functools
from typing import List
import time
import pandas as pd
import numpy as np
from tqdm import tqdm
import math
import sys
from model.quantize import *


@torch.no_grad()
def get_reorder_index(model, act_scales, metric='mean'):
    act_orders = {}
    def is_permutation(x: torch.Tensor) -> bool:
        if not torch.is_tensor(x) or x.dim() != 1:
            return False
            
        if x.dtype.is_floating_point:
            return False
    
        n = len(x)
    
        if n == 0:
            return True
    
        expected = torch.arange(n, device=x.device, dtype=x.dtype)
        
        return torch.equal(torch.sort(x).values, expected)
    def reorder_tensor(tensor):
        # assert dimension == 1
        assert tensor.dim() == 1, "Choosing outliers must be 1 dimensional"
        sorted_tensor, sorted_index = torch.sort(tensor, descending=False) # For putting outliers at last
        # _, sorted_index = torch.sort(tensor, descending=True) # For putting outliers at first
        assert is_permutation(sorted_index)
        return sorted_index
        # return torch.arange(tensor.shape[0])
        
    for name, m in model.model.named_modules():
        if isinstance(m, nn.Linear):
            m.name = name
            # Reorder Index of each layer's input
            # Used to reorder the weight and previous layer's output
            inputName = name + ".input"
            # act_orders[inputName] = reorder_tensor(act_scales[inputName])
            # if metric == 'frobenius': 
            #     importance = torch.linalg.norm(m.weight.data, ord=2, dim=0) * act_scales[inputName]
            # else: 
            #     importance = act_scales[inputName]
            act_orders[inputName] = reorder_tensor(act_scales[inputName])
            # act_orders[inputName] = reorder_tensor(importance)

            assert act_orders[inputName].dim() == 1, "Return Index must be 1 dimensional"

    return act_orders



def load_model(model_path):
    config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
    config.use_cache = False
    kwargs = {"torch_dtype": "auto", "low_cpu_mem_usage": True}
    model = AutoModelForCausalLM.from_pretrained(model_path, config=config, trust_remote_code=True, **kwargs)
    model.eval()
    enc = AutoTokenizer.from_pretrained(model_path, use_fast=True, trust_remote_code=False)
    return model, enc



@torch.no_grad()
def get_act_stats(model, dataloader, device_, metric='mean', seqlen=2048):
    nsamples = len(dataloader)
    device = device_
    act_scales = {}

    def stat_tensor(name, tensor, weight=None):
        hidden_dim = tensor.shape[-1]
        tensor = tensor.view(-1, hidden_dim).detach()

        if metric == 'hessian':
            tensorH = math.sqrt(2 / nsamples) * tensor.float().t()
            comming_H = tensorH.matmul(tensorH.t())
            comming_scales = torch.diag(comming_H)
        elif metric == 'frobenius':
            tensorE = tensor - quantize_nvfp4_tensor(tensor, group_size=16)
            # tensorE = tensor - quantize_mxfp4_tensor(tensor, group_size=32)
            # tensorE = tensor - quantize_int4_tensor(tensor, group_size=128)
            if weight is not None:
                comming_scales = torch.linalg.norm(tensorE, ord=2, dim=0).float().cpu() * torch.linalg.norm(weight, ord=2, dim=0).float().cpu()
            else:
                comming_scales = torch.linalg.norm(tensorE, ord=2, dim=0).float().cpu()
        else:
            # Here we use abs since symmetric quantization use absmax.
            comming_scales = torch.mean(tensor.abs(), dim=0).float().cpu()

        if name in act_scales:
            if metric == 'hessian':
                act_scales[name] += comming_scales
            else:
                act_scales[name] = torch.max(act_scales[name], comming_scales)
        else:
            act_scales[name] = comming_scales

    def stat_input_hook(m, x, y, name):
        if isinstance(x, tuple):
            x = x[0]
            assert isinstance(x, torch.Tensor)
        if isinstance(y, tuple):
            y = y[0]
            assert isinstance(y, torch.Tensor)
        # stat_tensor(name + ".input", x, weight=m.weight.data)
        # stat_tensor(name + ".output", y, weight=m.weight.data)
        if ('o_proj' in name or 'down_proj' in name) and (metric == 'frobenius'):
            stat_tensor(name + ".input", x, weight=m.weight.data)
        else:
            stat_tensor(name + ".input", x)
        stat_tensor(name + ".output", y)

    hooks = []
    for name, m in model.model.named_modules():
        if isinstance(m, nn.Linear):
            hooks.append(
                m.register_forward_hook(
                    functools.partial(stat_input_hook, name=name)
                )
            )

    layers = model.model.layers
    model.model.embed_tokens = model.model.embed_tokens.to(device)
    if not model.model.norm.weight.is_meta:
        model.model.norm = model.model.norm.to(device)
    layers[0] = layers[0].to(device)

    dtype = next(iter(model.parameters())).dtype
    inps = torch.zeros(
        (nsamples, seqlen, model.config.hidden_size), dtype=dtype, device=device
    )
    cache = {'i': 0, 'attention_mask': None}

    class Catcher(nn.Module):
        def __init__(self, module):
            super().__init__()
            self.module = module
            self.self_attn = module.self_attn
        def forward(self, inp, **kwargs):
            inps[cache['i']] = inp.squeeze(0)
            cache['i'] += 1
            cache['attention_mask'] = kwargs['attention_mask']
            cache['position_ids'] = kwargs['position_ids']
            raise ValueError
    layers[0] = Catcher(layers[0])
    model.to(device)
    for batch in dataloader:
        try:
            model(batch[0].to(device))
        except ValueError:
            pass
    assert cache['i'] == nsamples, "Captured samples should be equal to nsamples"
    
    layers[0] = layers[0].module
    layers[0] = layers[0].cpu()
    model.model.embed_tokens = model.model.embed_tokens.cpu()
    if not model.model.norm.weight.is_meta:
        model.model.norm = model.model.norm.cpu()
    torch.cuda.empty_cache()

    outs = torch.zeros_like(inps)
    attention_mask = cache['attention_mask']
    position_ids = cache['position_ids']

    for i in tqdm(range(len(layers))):
        layer = layers[i].to(device)
        for j in range(nsamples):
            outs[j] = layer(inps[j].unsqueeze(0), attention_mask=attention_mask, position_ids=position_ids)[0]
        layers[i] = layer.cpu()
        del layer
        inps, outs = outs, inps

    for h in hooks:
        h.remove()

    return act_scales

    

def get_wikitext2(nsamples, seed, seqlen, tokenizer):
    from datasets import load_dataset
    traindata = load_dataset('wikitext', 'wikitext-2-raw-v1', split='train')
    testdata = load_dataset('wikitext', 'wikitext-2-raw-v1', split='test')
    trainenc = tokenizer("\n\n".join(traindata['text']), return_tensors='pt')
  
    import random
    random.seed(seed)
    trainloader = []
    inps = []
    for _ in range(nsamples):
        i = random.randint(0, trainenc.input_ids.shape[1] - seqlen - 1)
        j = i + seqlen
        inp = trainenc.input_ids[:, i:j]
        tar = inp.clone()
        tar[:, :-1] = -100
        trainloader.append((inp, tar))
        inps.append(inp)
    return trainloader, inps 


@torch.no_grad()
def search_select_proportions(model, dataloader, device_, seqlen, reorder_index, hessian):
    nsamples = len(dataloader)
    device = device_
    
    select_nums = {}
    average_bits = {}
   
    def stat_input_hook(m, x, y, name):
        if isinstance(x, tuple):
            x = x[0]
            assert isinstance(x, torch.Tensor)
        if isinstance(y, tuple):
            y = y[0]
            assert isinstance(y, torch.Tensor)
        act_scales[name+".input"] = x
        act_scales[name+".output"] = y
     
    hooks = []
    for name, m in model.model.named_modules():
        if isinstance(m, nn.Linear):
            hooks.append(
                m.register_forward_hook(
                    functools.partial(stat_input_hook, name=name)
                )
            )

    layers = model.model.layers
    model.model.embed_tokens = model.model.embed_tokens.to(device)
    if not model.model.norm.weight.is_meta:
        model.model.norm = model.model.norm.to(device)
    layers[0] = layers[0].to(device)

    dtype = next(iter(model.parameters())).dtype
    inps = torch.zeros(
        (nsamples, seqlen, model.config.hidden_size), dtype=dtype, device=device
    )
    cache = {'attention_mask': None}

    class Catcher(nn.Module):
        def __init__(self, module):
            super().__init__()
            self.module = module
            self.self_attn = module.self_attn
        def forward(self, inp, **kwargs):
            cache['inps'] = inp
            cache['attention_mask'] = kwargs['attention_mask']
            cache['position_ids'] = kwargs['position_ids']
            raise ValueError
    layers[0] = Catcher(layers[0])
    model.to(device)

    dataloader = torch.stack(dataloader, dim=0).squeeze(1)

    try:
        model(torch.tensor(dataloader).to(device))
    except ValueError:
        pass

    
    layers[0] = layers[0].module
    layers[0] = layers[0].cpu()
    model.model.embed_tokens = model.model.embed_tokens.cpu()
    if not model.model.norm.weight.is_meta:
        model.model.norm = model.model.norm.cpu()
    torch.cuda.empty_cache()

    inps = cache['inps']
  
    attention_mask = cache['attention_mask']
    position_ids = cache['position_ids']
  
    for i in tqdm(range(len(layers))):
        act_scales = {}
        layer = layers[i].to(device)
  
        inps = layer(inps, attention_mask=attention_mask, position_ids=position_ids)[0]
       
        for name, keys in act_scales.items():
            if 'output' in name:
                continue
                
            keys = keys.reshape(-1, keys.shape[-1]).contiguous()
            seqlen, in_features = keys.shape 
     
            select_ratio = 0.04
            select_num = math.ceil(in_features * select_ratio / 64) * 64
            average_bits[name] = 9 * select_ratio + 4.5 * (1.0 - select_ratio)
            
            print(f'select_num is {select_ratio}, avg:{average_bits[name]}')
            select_nums[name] = select_num

            del keys
            
            gc.collect()
            torch.cuda.empty_cache()
            
        
        
        layer.cpu()
        del act_scales
        del layer
        gc.collect()
        torch.cuda.empty_cache()
            

    for h in hooks:
        h.remove()

    return select_nums, average_bits