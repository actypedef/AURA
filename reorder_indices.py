from datasets import load_dataset
import torch.nn as nn
import gc
from utilize import *
import torch
from collections import defaultdict
from model import quantize_nvfp4_tensor
import functools
from typing import List
import time
import pandas as pd
import numpy as np
import tqdm
import argparse
import math
import os
import time


parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, help="path of the hf model")
parser.add_argument("--act_sort_metric", type=str, help="the metric used to sort the activations.")
parser.add_argument("--samples", type=int, default=128)
parser.add_argument("--seqlen", type=int, default=2048)


args = parser.parse_args()


        
def main():
    model, enc = load_model(args.model)
    folder_path = "./saved"
    path = args.model.rstrip('/')
    model_name = path.split('/')[-1]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    #reorder
    
    start_time = time.time()
    print("Getting activation stats...")
    
    if not os.path.exists(f'./saved/{model_name.lower()}_act_scales_wikitext2_{args.act_sort_metric}.pt'):
        dataloader, _ = get_wikitext2(
                nsamples=args.samples, seed=0, tokenizer=enc, seqlen=args.seqlen
            )

        act_scales = get_act_stats(
            model, dataloader, "cuda:0", metric=args.act_sort_metric, seqlen=args.seqlen
        )
        torch.save(act_scales, f'./saved/{model_name.lower()}_act_scales_wikitext2_{args.act_sort_metric}.pt')
        del dataloader
    else:
        act_scales = torch.load(f'./saved/{model_name.lower()}_act_scales_wikitext2_{args.act_sort_metric}.pt')
    print("Getting reording index...")
    
    reorder_index = get_reorder_index(model, act_scales, metric=args.act_sort_metric)
    
    print("Getting proportions...")
    _, inps = get_wikitext2(
                nsamples=args.samples, seed=0, tokenizer=enc, seqlen=args.seqlen
            )
    select_num, average_bits = search_select_proportions(model, inps, "cuda:0", args.seqlen, reorder_index, act_scales)
    print(time.time()-start_time)

    torch.save(reorder_index, f'./saved/{model_name.lower()}_reorder_index_wikitext2_{args.act_sort_metric}.pt')
    torch.save(select_num, f'./saved/{model_name.lower()}_select_num_wikitext2_{args.act_sort_metric}.pt')
    torch.save(average_bits, f'./saved/{model_name.lower()}_average_bits_wikitext2_{args.act_sort_metric}.pt')
    
if __name__ == "__main__":
    main()
