from typing import List

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from base import DecoderBase
from utility import (
    extra_eos_for_direct_completion,
    make_raw_chat_prompt,
)

class QuantizationConfig:
    def __init__(self):
        # Model and dataset parameters
        self.save_dir = './saved'
        self.dataset = 'wikitext2'
        # Quantization bits
        self.wbits = 4  # weight bits
        self.abits = 4  # activation bits
        
        # Symmetry and exponential settings
        self.exponential = False
        self.a_sym = True  # activation symmetry
        self.w_sym = True  # weight symmetry
        self.static = False
        
        # Grouping settings
        self.weight_group_size = 128
        self.weight_channel_group = 2
        self.act_group_size = 128
        
        # Reorder and sorting settings
        self.reorder = True
        self.act_sort_metric = 'mean'
        
        # Keeper settings
        self.keeper = 128
        self.keeper_precision = 3
        
        # Tiling and KV cache
        self.tiling = 0
        self.kv_cache = False
        
        # Clip ratios
        self.a_clip_ratio = 0.9  # activation clip ratio
        self.w_clip_ratio = 0.85  # weight clip ratio
        self.kv_clip_ratio = 1.0  # KV cache clip ratio
        
        # Quantization type
        self.quant_type = 'int'
        
    def __str__(self):
        """Return a string representation of all parameters"""
        params = vars(self)
        return "\n".join(f"{k}: {v}" for k, v in params.items())
    
    def to_dict(self):
        """Return parameters as a dictionary"""
        return vars(self)
        
class HuggingFaceDecoder(DecoderBase):
    def __init__(
        self,
        name: str,
        dataset: str,
        force_base_prompt: bool = False,
        attn_implementation: str = "eager",
        device_map: str = None,
        gguf_file: str = None,
        **kwargs,
    ):
        super().__init__(name=name, **kwargs)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        kwargs = {
            "device_map": "cpu",
            "trust_remote_code": self.trust_remote_code,
            "torch_dtype": getattr(torch, self.dtype),
            "attn_implementation": attn_implementation,  # "eager", "flash_attention_2", "sdpa"
            "gguf_file": gguf_file
        }

        self.skip_special_tokens = True

        print(f"{kwargs = }")

        self.force_base_prompt = force_base_prompt

        # gguf format embeds tokenizer and is not compatible with hf tokenizer `use_fast` param
        tokenizer_kwargs = {}
        if gguf_file is not None:
            tokenizer_kwargs["gguf_file"] = gguf_file
        self.tokenizer = AutoTokenizer.from_pretrained(name, **tokenizer_kwargs)
        if self.is_direct_completion():  # no chat template
            self.eos += extra_eos_for_direct_completion(dataset)
        else:  # with chat template
            self.eos += ["\n```\n"]
        model_name = name.split('/')[-2]
        print(f"{self.eos = }")
        self.model = AutoModelForCausalLM.from_pretrained(name, **kwargs)
    
        
        from modelutils_qwen import reorder_model_qwen
        
        index_filename = f'/root/autodl-tmp/AURA/saved/{model_name.lower()}_reorder_index_wikitext2_frobenius.pt'
        select_num_filename = f'/root/autodl-tmp/AURA/saved/{model_name.lower()}_select_num_wikitext2_frobenius.pt'
        reorder_index = torch.load(index_filename, weights_only=False)
        select_nums = torch.load(select_num_filename, weights_only=False)
        
        self.model = reorder_model_qwen(self.model, device='cuda', kv_cache=False, reorder_index=reorder_index, select_nums=select_nums)
        
        self.model = self.model.to(self.device)
        print(self.model)
    def is_direct_completion(self) -> bool:
        return self.force_base_prompt or self.tokenizer.chat_template is None

    @torch.inference_mode()
    def codegen(
        self, prompt: str, do_sample: bool = True, num_samples: int = 200
    ) -> List[str]:
        if self.temperature == 0:
            assert not do_sample
            assert num_samples == 1

        # assert (self.is_direct_completion())

        prompt = (
            f"""<|im_start|>system
You are an intelligent programming assistant to produce Python algorithmic solutions<|im_end|>
<|im_start|>user
Can you complete the following Python function?
```python
{prompt}
```
<|im_end|>
<|im_start|>assistant
```python
"""
            if self.is_direct_completion()
            else make_raw_chat_prompt(
                prompt, self.instruction_prefix, self.response_prefix, self.tokenizer
            )
        )
        input_tokens = self.tokenizer.encode(prompt, return_tensors="pt").to(
            self.device
        )
        kwargs = {}
        if do_sample:
            kwargs["top_p"] = 0.95
            kwargs["temperature"] = self.temperature

        outputs = self.model.generate(
            input_tokens,
            max_new_tokens=self.max_new_tokens,
            do_sample=do_sample,
            num_return_sequences=min(self.batch_size, num_samples),
            pad_token_id=self.tokenizer.pad_token_id or self.tokenizer.eos_token_id,
            stop_strings=self.eos,
            tokenizer=self.tokenizer,
            **kwargs,
        )

        gen_strs = self.tokenizer.batch_decode(
            outputs[:, input_tokens.size(-1) :],
            skip_special_tokens=self.skip_special_tokens,
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index].replace("\t", "    "))
        return outputs