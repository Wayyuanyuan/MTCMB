import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

from make_answer.chat.chat_invoker import ChatInvoker


class LocalHuaTuo2(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int=0):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, device_map={"": gpu_id}, torch_dtype=torch.bfloat16, trust_remote_code=True)
        self.model.generation_config = GenerationConfig.from_pretrained(model_path)

    def chat(
        self, msg: str, *args, **kwargs
    ) -> str:
        messages = []
        if "role_prompt" in kwargs:
            role_prompt = kwargs["role_prompt"]
            messages = [{"role": "user", "content": role_prompt + msg}]
        else:
            messages = [{"role": "user", "content": msg}]
        return self.model.HuatuoChat(self.tokenizer, messages)
