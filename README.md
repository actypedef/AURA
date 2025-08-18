# 😇AURA: Augmented Representation for Unified Accuracy-aware Quantization

AURA is a quantization method that quantizes both weight and activation to low-bit augmented matrices. 


We use an accuracy-aware strategy to determine which channels are more likely to suffer severe accuracy loss when performing low-bit quantization. Then we quantize the weight and activation to NVFP4 augmented matrices, concating additional channels to contain the quantize error in activation matrices. 


In contrast to traditional mixed-precision quantization methods, AURA decouples the GEMM kernel from the quantization process. This design enables support for various data formats, such as MXFP4 and NVFP4, and facilitates easier adaptation to future data types, establishing it as a more universal strategy. 


## 1. Installation
```bash
conda create -n aura python=3.10 -y
conda activate aura
```
Please make sure that [CUDA 12.8](https://developer.nvidia.com/cuda-12-8-1-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=runfile_local) is in your environment.
```bash
git clone --recurse-submodules https://github.com/actypedef/AURA.git
cd AURA
pip install -r requirements.txt
```

## 2. Usage

### 2.1 Preprocessing
Reorder_indices, select_num are needed for quantization:
```bash
python reorder_indices.py --model /PATH/TO/YOUR/MODEL/ --samples 32 --seqlen 2048 --act_sort_metric frobenius
```
Results are saved in ./saved/
### 2.2 Building Kernels
Please refer to `kernels/README.md`
```bash
cd kernels/
```
### 2.3 Accuracy Evaluation
```bash
bash run_micromix.sh /PATH/TO/YOUR/MODEL/
```

## 3. Efficiency Evaluation
Since [FlashInfer](https://github.com/flashinfer-ai/flashinfer/tree/main) is integrated into our decoderlayer implementation, please install FlashInfer:
```bash
git clone --recurse-submodules https://github.com/flashinfer-ai/flashinfer.git
cd flashinfer
python -m pip install -v .
```
DecoderLayer efficiency:
```bash
python benchmarks/benchmark_layer_aura.py --model 'llama-3.1-8b' --batch_size 32 --prefill_seq_len 2048
```
TensorRT efficiency:
```bash
pip install tensorrt
python benchmark/trt-fp8-prefill-llama.py
```

| Llama-3.1-8b  | ARC_C | BoolQ | LAMBADA | PIQA  | Winogrande | Avg   | MMLU  | wikitext | 
|---            |---    |---    |---      |---    |---         |---    |---    |---       |
| FP16          | 51.28 | 82.05 | 75.80   | 80.03 | 73.64      | 72.56 | 65.40 | 5.60     |
| QuaRot        | 46.42 | 76.24 | 68.48   | 77.91 | 70.96      | 68.00 | 55.23 | 6.98     |
| QUIK          | 44.62 | 77.09 | 73.28   | 77.09 | 69.19      | 68.05 | 56.65 | 7.29     |
| Atom          | 50.17 | 76.15 | 69.45   | 78.02 | 70.01      | 68.76 | 58.05 | 6.79     |
| AMXFP4        | 43.77 | 74.80 | 71.12   | 75.19 | 66.85      | 66.34 | 53.79 | 7.49     |
| MicroMix      | 49.74 | 80.18 | 72.64   | 78.29 | 70.80      | 70.33 | 58.47 | 6.72     |
| AURA-nv(100%) | 50.51 | 79.91 | 73.74   | 80.58 | 73.40      | 71.63 | -     | 6.84     |
| AURA-nv(40%)  | 50.77 | 79.33 | 72.52   | 80.52 | 72.53      | 71.13 | 61.17 | 6.97     |
| AURA-nv(20%)  | 49.57 | 79.17 | 72.91   | 80.14 | 72.06      | 70.78 | 61.00 | 7.02     |
| AURA-nv(15%)  | 49.23 | 79.36 | 72.40   | 80.03 | 73.01      | 70.81 | 61.05 | 7.05     |
| AURA-nv(10%)  | 49.74 | 78.93 | 72.33   | 80.69 | 72.30      | 70.80 | 60.90 | 7.07     |
| AURA-nv( 5%)  | 49.49 | 78.62 | 72.52   | 79.65 | 72.14      | 70.48 | 60.21 | 7.09     |
| nvfp4         | 49.15 | 77.95 | 70.97   | 79.38 | 70.80      | 69.65 | 60.75 | 7.18     |
| MEAN-nv(20%)  | 50.43 | 79.51 | 71.82   | 80.30 | 72.53      | 70.92 | -     | 7.00     |
| MEAN-nv(10%)  | 50.26 | 78.29 | 71.86   | 80.36 | 70.80      | 70.31 | 61.34 | 7.02     |
| MEAN-nv( 5%)  | 49.15 | 78.81 | 71.51   | 80.52 | 71.67      | 70.33 | 61.29 | 7.06     |
| FAKE-mx(40%)  | 50.17 | 78.07 | 71.63   | 79.82 | 71.51      | 70.24 | -     | -        |
| FAKE-mx(20%)  | 49.32 | 78.26 | 72.17   | 79.16 | 70.01      | 69.78 | -     | -        |
| FAKE-mxfp4    | 47.44 | 75.05 | 69.38   | 78.67 | 69.46      | 68.00 | -     | -        |



| Llama-2-7b    | ARC_C | BoolQ | LAMBADA | PIQA  | Winogrande | Avg   | MMLU  | wikitext | 
|---            |---    |---    |---      |---    |---         |---    |---    |---       |
| AURA-nv(10%)  | 45.14 | 75.29 | 72.13   | 78.13 | 68.03      | 67.75 | 41.25 | 5.77     |
| AURA-nv( 5%)  | 44.37 | 75.32 | 72.56   | 77.97 | 67.09      | 67.46 | 41.11 | 5.78     |
| MEAN-nv(10%)  | 45.15 | 75.87 | 72.25   | 77.97 | 68.51      | 67.95 | 39.88 | 5.75     |
| MEAN-nv( 5%)  | 44.28 | 75.99 | 72.93   | 78.67 | 67.32      | 67.84 | 39.98 | 5.76     |
| nvfp4         | 43.69 | 75.87 | 72.93   | 78.02 | 68.43      | 67.79 | 40.37 | 5.83     |


| Qwen-2.5-7b   | ARC_C | BoolQ | LAMBADA | PIQA  | Winogrande | Avg   | MMLU  | wikitext | 
|---            |---    |---    |---      |---    |---         |---    |---    |---       |
| FP16          | 55.20 | 83.55 | 72.35   | 79.87 | 72.65      | 72.76 | 72.93 | -        |
| AURA-nv(10%)  | 51.71 | 83.67 | 71.80   | 79.60 | 70.72      | 71.50 | 72.02 | 7.30     |
| MEAN-nv(10%)  | 52.13 | 83.76 | 69.53   | 78.89 | 72.06      | 71.27 | 72.53 | 7.30     |
| nvfp4         | 50.77 | 82.84 | 70.83   | 78.73 | 69.14      | 70.46 | 71.79 | 7.40     |

| Llama-3.1-8b  | ARC_C | BoolQ | LAMBADA | PIQA  | Winogrande | Avg   | MMLU  | wikitext | 
|---            |---    |---    |---      |---    |---         |---    |---    |---       |
| FAKE-nv(40%)  | 49.83 | 80.70 | 74.05   | 79.76 | 73.01      | 71.47 | 62.93 | 6.81     |
| FAKE-nv(20%)  | 50.00 | 80.03 | 74.50   | 79.87 | 72.85      | 71.45 | 62.88 | 6.87     |
| FAKE-nv(10%)  | 50.77 | 80.98 | 74.11   | 80.03 | 72.06      | 71.59 | 62.43 | 6.91     |
| FAKE-nv( 5%)  | 50.35 | 80.52 | 73.69   | 79.98 | 72.22      | 71.35 | 62.80 | 6.92     |
| FAKE-nv(2.5%) | 50.34 | 80.15 | 73.94   | 80.36 | 70.80      | 71.12 | 62.80 | 6.92     |
