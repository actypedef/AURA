from datasets import load_dataset
import torch.nn as nn
import gc
from utilize import * # 确保 get_c4 和 get_pile 在这里
import torch
from collections import defaultdict
# from model import quantize_nvfp4_tensor # 如果需要，请取消注释
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
# 添加 --dataset 参数用于选择校准集
parser.add_argument(
    "--dataset", type=str, default="wikitext2", choices=["wikitext2", "c4", "humaneval"], 
    help="The calibration dataset to use."
)
parser.add_argument("--act_sort_metric", type=str, help="the metric used to sort the activations.")
parser.add_argument("--samples", type=int, default=128)
parser.add_argument("--seqlen", type=int, default=2048)


args = parser.parse_args()


# 定义一个字典来简化函数调用
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
    
    # ----- 数据加载和处理 -----
    print(f"Using {args.dataset} dataset for calibration.")
    # 从字典中获取对应的数据集加载函数
    get_dataset = DATASET_LOADERS[args.dataset]

    # 根据数据集动态生成文件名
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
    select_num, average_bits = search_select_proportions(model, "cuda:0", args.seqlen, reorder_index, act_scales)
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

    # ----- 保存结果 -----
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