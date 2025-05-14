import re

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalWiNGPT2(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int = 0):
        self.__device = f'cuda:{gpu_id}'
        self.__model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map=self.__device
        )
        self.__model.eval()
        self.__tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        role_prompt = ""
        if "role_prompt" in kwargs:
            role_prompt = kwargs["role_prompt"]
        user_input = f'User:{role_prompt + msg}<|endoftext|>\n Assistant:'
        inputs = self.__tokenizer.encode(user_input, return_tensors="pt").to(self.__device)
        outputs = self.__model.generate(inputs, repetition_penalty=1.1, max_new_tokens=1024)
        response = self.__tokenizer.decode(outputs[0])
        pattern = r'Assistant:(.*?)<\|endoftext\|>'
        match = re.search(pattern, response, re.DOTALL)
        if match:
            response = match.group(1).strip()

        return response


if __name__ == '__main__':
    llm = LocalWiNGPT2("/mnt/data1/MedLLM_baselines/WiNGPT2-14B-Chat", 5)
    print(llm.chat("我肚子疼，是什么原因导致的？"))
    print('*' * 200)
    print(llm.chat("我该吃什么药？"))
