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
from model.kv_cache import *


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
    
    if hasattr(model.model, 'rotary_emb'):
        model.model.rotary_emb = model.model.rotary_emb.to(device)
    
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
        gc.collect()

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

def get_c4(nsamples, seed, seqlen, tokenizer):
    from datasets import load_dataset
    import random

    dataset = load_dataset(
        'allenai/c4', 'en', 
        split='train', 
        streaming=True, 
        trust_remote_code=True
    )
    
    shuffled_dataset = dataset.shuffle(buffer_size=10000, seed=seed)

    trainloader = []
    inps = []
    for data in shuffled_dataset:
        if len(inps) == nsamples:
            break

        text = data.get('text', '')
        if not text:
            continue

        enc = tokenizer(text, return_tensors='pt')

        if enc.input_ids.shape[1] >= seqlen:
            i = random.randint(0, enc.input_ids.shape[1] - seqlen - 1)
            j = i + seqlen
            inp = enc.input_ids[:, i:j]
            tar = inp.clone()
            tar[:, :-1] = -100
            
            trainloader.append((inp, tar))
            inps.append(inp)
            
    if len(inps) < nsamples:
        print(f"warning: only get {len(inps)} samples >= {seqlen} ")

    return trainloader, inps


def get_humaneval(nsamples, seed, seqlen, tokenizer):
    import random
    
    try:
        from human_eval.data import read_problems
        problems = read_problems()  
        dataset = list(problems.values())
    except ImportError:
        print("=" * 80)
        print("run 'pip install humaneval'")
        print("=" * 80)
        return [], []
    except Exception as e:
        print(f" 'humaneval' loading error: {e}")
        return [], []

    text_corpus = "\n\n".join([sample['prompt'] for sample in dataset])
    trainenc = tokenizer(text_corpus, return_tensors='pt')

    random.seed(seed)
    trainloader = []
    inps = []
    for _ in range(nsamples):
        if trainenc.input_ids.shape[1] <= seqlen:
            print(f"warning: HumanEval total length ({trainenc.input_ids.shape[1]}) <= seqlen ({seqlen}).")
            inp = trainenc.input_ids
        else:
            i = random.randint(0, trainenc.input_ids.shape[1] - seqlen - 1)
            j = i + seqlen
            inp = trainenc.input_ids[:, i:j]

        tar = inp.clone()
        tar[:, :-1] = -100
        trainloader.append((inp, tar))
        inps.append(inp)
        
        if trainenc.input_ids.shape[1] <= seqlen:
            break 

    return trainloader, inps

@torch.no_grad()
def search_select_proportions(model, device_, seqlen, reorder_index, select_ratio=0.06):

    select_nums = {}
    average_bits = {}

    for name, m in model.model.named_modules():
        if 'output' in name:
                continue
        if isinstance(m, nn.Linear):
            in_features = m.in_features
            
            select_num = math.ceil(in_features * select_ratio / 64) * 64
            
            dict_key = name + ".input"
            
            average_bits[dict_key] = 9 * select_ratio + 4.5 * (1.0 - select_ratio)
            select_nums[dict_key] = select_num


    return select_nums, average_bits