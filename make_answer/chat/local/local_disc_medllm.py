import importlib.util
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
import transformers.modeling_utils as _modeling_utils

from make_answer.chat.chat_invoker import ChatInvoker


def _load_build_chat_input(model_path: str):
    spec = importlib.util.spec_from_file_location(
        "disc_generation_utils",
        os.path.join(model_path, "generation_utils.py"),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.build_chat_input


class LocalDiscMedLLM(ChatInvoker):
    """DISC-MedLLM（Baichuan-13B），用法同官方 README（build_chat_input + generate）。"""

    def __init__(self, model_path: str, gpu_id: int = 0):
        n_gpu = torch.cuda.device_count()
        if gpu_id < 0 or gpu_id >= n_gpu:
            raise ValueError(
                f"GPU {gpu_id} 不可用：当前进程可见 {n_gpu} 张卡（编号 0–{n_gpu - 1}）。"
                "请检查 --num-gpus 或 shell 中的 CUDA_VISIBLE_DEVICES。"
            )
        self._build_chat_input = _load_build_chat_input(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, use_fast=False, trust_remote_code=True,
        )
        _orig_check = _modeling_utils.check_torch_load_is_safe
        _modeling_utils.check_torch_load_is_safe = lambda: None
        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.float16,
                trust_remote_code=True,
                device_map={"": gpu_id},
            )
        finally:
            _modeling_utils.check_torch_load_is_safe = _orig_check
        self.model.eval()
        self.model.generation_config = GenerationConfig.from_pretrained(model_path)
        self.__device = self.model.device

    def chat(self, msg: str, *args, **kwargs) -> str:
        if "role_prompt" in kwargs:
            msg = kwargs["role_prompt"] + msg
        messages = [{"role": "user", "content": msg}]
        input_ids = self._build_chat_input(
            self.model, self.tokenizer, messages,
        )
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids,
                generation_config=self.model.generation_config,
                use_cache=False,
            )
        return self.tokenizer.decode(
            outputs[0][input_ids.shape[-1]:], skip_special_tokens=True,
        ).strip()
