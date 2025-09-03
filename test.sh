mkdir -p results/humaneval
export HF_ENDPOINT=https://hf-mirror.com
export PATH=./vllm/bin:$PATH
export PYTHONPATH=$PYTHONPATH:./eval_plus/evalplus
MODEL_DIR=${1}
# pip install datamodel_code_generator anthropic mistralai google-generativeai

MODEL_DIR=${MODEL_DIR:-"/root/autodl-tmp/Qwen2.5-Coder-32B/"}
TP=${2}
TP=${TP:-1}
OUTPUT_DIR=${3}
OUTPUT_DIR=${OUTPUT_DIR:-"./eval_plus/output"}
MODEL_SIZE='32B'
mkdir -p ${OUTPUT_DIR}

echo "EvalPlus: ${MODEL_DIR}, OUTPUT_DIR ${OUTPUT_DIR}"

python ./eval_plus/generate.py \
  --model_type codeqwen \
  --model_size ${MODEL_SIZE} \
  --model_path ${MODEL_DIR} \
  --bs 1 \
  --temperature 0 \
  --n_samples 1 \
  --greedy \
  --root ${OUTPUT_DIR} \
  --dataset humaneval \
  --tensor-parallel-size ${TP}


# # python -m evalplus.sanitize --samples ${OUTPUT_DIR}/humaneval/qwen2_${MODEL_SIZE}_temp_0.0


evalplus.evaluate \
  --dataset humaneval \
  --samples ${OUTPUT_DIR}/humaneval/qwen2_${MODEL_SIZE}_temp_0.0 > ${OUTPUT_DIR}/humaneval/raw_humaneval_${MODEL_SIZE}_results.txt

# evalplus.evaluate \
#   --dataset humaneval \
#   --samples ${OUTPUT_DIR}/humaneval/qwen2_${MODEL_SIZE}_temp_0.0-sanitized > ${OUTPUT_DIR}/humaneval_results.txt


python ./eval_plus/generate.py \
  --model_type qwen2 \
  --model_size ${MODEL_SIZE} \
  --model_path ${MODEL_DIR} \
  --bs 1 \
  --temperature 0 \
  --n_samples 1 \
  --greedy \
  --root ${OUTPUT_DIR} \
  --dataset mbpp \
  --tensor-parallel-size ${TP}


# # python -m evalplus.sanitize --samples ${OUTPUT_DIR}/mbpp/qwen2_${MODEL_SIZE}_temp_0.0


evalplus.evaluate \
  --dataset mbpp \
  --samples ${OUTPUT_DIR}/mbpp/qwen2_${MODEL_SIZE}_temp_0.0 > ${OUTPUT_DIR}/mbpp/raw_mbpp_${MODEL_SIZE}_results.txt

# evalplus.evaluate \
#   --dataset mbpp \
#   --samples ${OUTPUT_DIR}/mbpp/qwen2_${MODEL_SIZE}_temp_0.0-sanitized > ${OUTPUT_DIR}/mbpp/mbpp_${MODEL_SIZE}_results.txt