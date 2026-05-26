import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

from make_answer.chat.chat_invoker import ChatInvoker


class LocalBaichuan(ChatInvoker):
    """Baichuan-M1-14B-Instruct，用法同官方 README（apply_chat_template）。"""

    def __init__(self, model_path: str, gpu_id: int = 0):
        n_gpu = torch.cuda.device_count()
        if gpu_id < 0 or gpu_id >= n_gpu:
            raise ValueError(
                f"GPU {gpu_id} 不可用：当前进程可见 {n_gpu} 张卡（编号 0–{n_gpu - 1}）。"
                "请检查 --num-gpus 或 shell 中的 CUDA_VISIBLE_DEVICES。"
            )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True,
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map={"": gpu_id},
            attn_implementation="eager",
        )
        self.model.eval()

        gen_config = GenerationConfig.from_pretrained(model_path)
        if gen_config.top_k is None or gen_config.top_k <= 0:
            gen_config.top_k = 5
        self.model.generation_config = gen_config
        self.__device = self.model.device

    def chat(self, msg: str, *args, **kwargs) -> str:
        if "role_prompt" in kwargs:
            msg = kwargs["role_prompt"] + msg
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.__device)
        with torch.no_grad():
            outputs = self.model.generate(
                **model_inputs,
                max_new_tokens=2048,
                do_sample=True,
            )
        input_len = model_inputs.input_ids.shape[-1]
        return self.tokenizer.decode(
            outputs[0][input_len:], skip_special_tokens=True,
        ).strip()
