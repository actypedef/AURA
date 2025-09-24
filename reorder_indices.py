from datasets import load_dataset
import torch.nn as nn
import gc
from utilize import * 
import torch
from collections import defaultdict
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
parser.add_argument(
    "--dataset", type=str, default="wikitext2", choices=["wikitext2", "c4", "humaneval"], 
    help="The calibration dataset to use."
)
parser.add_argument("--act_sort_metric", type=str, help="the metric used to sort the activations.")
parser.add_argument("--ratio", type=float, default=-1, help="compensation ratio for AURA.")
parser.add_argument("--samples", type=int, default=128)
parser.add_argument("--seqlen", type=int, default=2048)


args = parser.parse_args()


DATASET_LOADERS = {
    "wikitext2": get_wikitext2,
    "c4": get_c4,
    "humaneval": get_humaneval
}
        
def main():
    model, enc = load_model(args.model)
    folder_path = "./saved"
    path = args.model.rstrip('/')
    model_name = path.split('/')[-1]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    os.environ['HF_HUB_DOWNLOAD_TIMEOUT'] = '120'
    start_time = time.time()
    
    print(f"Using {args.dataset} dataset for calibration.")
    get_dataset = DATASET_LOADERS[args.dataset]

    dataset_name = args.dataset.lower()
    act_scales_filename = f'./saved/{model_name.lower()}_act_scales_{dataset_name}_{args.act_sort_metric}.pt'

    print("Getting activation stats...")
    if not os.path.exists(act_scales_filename):
        print("Generating activation stats...")
        dataloader, _ = get_dataset(
            nsamples=args.samples, seed=0, seqlen=args.seqlen, tokenizer=enc
        )

        act_scales = get_act_stats(
            model, dataloader, "cuda:0", metric=args.act_sort_metric, seqlen=args.seqlen
        )
        torch.save(act_scales, act_scales_filename)
        del dataloader
    else:
        print("Loading pre-saved activation stats...")
        act_scales = torch.load(act_scales_filename)

    print("Getting reording index...")
    reorder_index = get_reorder_index(model, act_scales, metric=args.act_sort_metric)
    
    print("Getting proportions...")

    if args.ratio >= 0 and args.ratio <= 1.0: 
        ratio = args.ratio
    elif 'llama' in model_name.lower():
        ratio = 0.04
    else:
        ratio = 0.06
    
    select_num, average_bits = search_select_proportions(model, "cuda:0", args.seqlen, reorder_index, select_ratio=ratio)
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    print(f"Compensation Ratio: {ratio * 100:.1f}%")

    reorder_filename = f'./saved/{model_name.lower()}_reorder_index_{dataset_name}_{args.act_sort_metric}.pt'
    select_num_filename = f'./saved/{model_name.lower()}_select_num_{dataset_name}_{args.act_sort_metric}.pt'
    avg_bits_filename = f'./saved/{model_name.lower()}_average_bits_{dataset_name}_{args.act_sort_metric}.pt'

    print(f"Saving reorder index to {reorder_filename}")
    torch.save(reorder_index, reorder_filename)
    print(f"Saving select num to {select_num_filename}")
    torch.save(select_num, select_num_filename)
    print(f"Saving average bits to {avg_bits_filename}")
    torch.save(average_bits, avg_bits_filename)
    
if __name__ == "__main__":
    main()