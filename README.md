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

## Acknowledagement
Our code is built on the following repos, thank you for your contributions to community 👍:
- [Atom](https://github.com/efeslab/Atom.git)
- [QuaRot](https://github.com/spcl/QuaRot)
- [FlashInfer](https://github.com/flashinfer-ai/flashinfer/tree/main)
- [CUTLASS](https://github.com/NVIDIA/cutlass)
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
