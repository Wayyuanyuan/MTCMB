import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalTaiYi(ChatInvoker):
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
        import logging
        logging.disable(logging.WARNING)
        self.__tokenizer.pad_token_id = self.__tokenizer.eod_id
        self.__tokenizer.bos_token_id = self.__tokenizer.eod_id
        self.__tokenizer.eos_token_id = self.__tokenizer.eod_id
        self.__max_new_tokens = 512
        self.__top_p = 0.9
        self.__temperature = 0.3
        self.__repetition_penalty = 1.1

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        if "role_prompt" in kwargs:
            user_input = kwargs["role_prompt"] + msg
        else:
            user_input = msg

        input_ids = self.__tokenizer(user_input, return_tensors="pt", add_special_tokens=False).input_ids
        bos_token_id = torch.tensor([[self.__tokenizer.bos_token_id]], dtype=torch.long)
        eos_token_id = torch.tensor([[self.__tokenizer.eos_token_id]], dtype=torch.long)
        user_input_ids = torch.concat([bos_token_id, input_ids, eos_token_id], dim=1)

        model_input_ids = user_input_ids.to(self.__device)
        with torch.no_grad():
            outputs = self.__model.generate(
                input_ids=model_input_ids, max_new_tokens=self.__max_new_tokens, do_sample=True, top_p=self.__top_p,
                temperature=self.__temperature, repetition_penalty=self.__repetition_penalty, eos_token_id=self.__tokenizer.eos_token_id
            )

        response = self.__tokenizer.batch_decode(outputs, skip_special_tokens=True)
        response = response[0].replace(user_input, "", 1).strip()

        return response

if __name__ == '__main__':
    llm = LocalTaiYi("/mnt/data1/MedLLM_baselines/Taiyi", 3)
    print(llm.chat("我肚子疼，是什么原因导致的？"))
    print('*'*200)
    print(llm.chat("我该吃什么药？"))