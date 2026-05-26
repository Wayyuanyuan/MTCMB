import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

from make_answer.chat.chat_invoker import ChatInvoker


class LocalHuaTuo2(ChatInvoker):
    """HuatuoGPT-o1-72B（Qwen2.5-72B），用法同官方 README。"""

    def __init__(self, model_path: str, gpu_id: int = 0):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_path, use_fast=True, trust_remote_code=True,
            )
        except Exception:
            # tokenizer.json 与旧版 tokenizers 库不兼容时回退 slow tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_path, use_fast=False, trust_remote_code=True,
            )

        # 72B 需多卡 auto 切分；单卡 device_map={"": gpu_id} 会 OOM
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
        )
        self.model.eval()

        gen_config = GenerationConfig.from_pretrained(model_path)
        if gen_config.top_k is None or gen_config.top_k <= 0:
            gen_config.top_k = 50
        self.model.generation_config = gen_config

    def chat(self, msg: str, *args, **kwargs) -> str:
        if "role_prompt" in kwargs:
            msg = kwargs["role_prompt"] + msg
        messages = [{"role": "user", "content": msg}]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=2048,
                do_sample=True,
                top_k=50,
                top_p=0.8,
                temperature=0.7,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
        return self.tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
