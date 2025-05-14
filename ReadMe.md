# MTCMB Multi-Task TCM Evaluation Benchmark

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>

![title](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/title2.png)

<p align="center">
   📃 <a href="" target="_blank">Paper</a> • 🌐 <a href="" target="_blank">Website</a>  
   <br>  <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe_cn.md">   中文</a> | <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe.md"> English
</p>




## 🌈 Update

- **[2025.5.15]** The research article has been released.
- **[2025.5.15]** 🎉🎉🎉The official release of the MTCMB guidelines is hereby announced!🎉🎉🎉

## 🌐 Data Download

（1）ZIP format

```python
  https://github.com/Wayyuanyuan/MTCMB.git && cd data
```

（2）[Baidu Netdisk Link](https://pan.baidu.com/s/1_pOlvjRNEbOp29oDPi7bRQ?pwd=vgzt)



## 📍Ranking List

## 😊Dataset Description


#### **Data Structure**

Dataset: **5** Dimensions, **12** Datasets

The following figure shows the data volume distribution in four dimensions: language understanding, diagnosis, prescription recommendation, and safety assessment:

![pie-nest](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/area-stack%20-en.png)

🥸 **Knowledge Question Answering Dimension** contains three data sets, namely TCM-ED-A (1200), TCM-ED-B (4800), TCM-FT (100)

- **Knowledge Question and Answer**: Test the LLM's understanding and application of core knowledge in basic theories of TCM, formula science, acupuncture, and diagnostics through questions from the Intermediate Attending Physician and Licensed Physician Examinations, as well as standard essay-style questions.

- **Language Understanding**: This dimension evaluates the performance of the LLM in TCM text understanding and information extraction through entity extraction in medical records, generating structured medical records from doctor-patient conversations, and answering questions based on literature content.

- **Diagnosis**: This dimension examines the ability of the LLM to conduct syndrome differentiation analysis based on the patient's clinical information (such as symptoms, signs, tongue and pulse, etc.) and accurately determine the name of the disease and syndrome type.

- **Prescription Recommendation**: This dimension assesses LLM's ability to recommend appropriate prescriptions based on the description of the disease and the characteristics of the syndrome. It specifically covers the understanding of the composition of the prescription, the rules of compatibility, and the correspondence between symptoms and diseases.

- **Safety evaluation**: This dimension evaluates the ability of the LLM to identify safety risks involved in TCM practice through fill-in-the-blank questions and multiple-choice questions.

####  Detailed Information

**By clicking the hyperlink, you can access the format requirements for various datasets.**

| Dimension                     | Dataset name                                                 | Quantity | Task description                                             | Data source                                                  | Construction method                                          | Evaluation method                                 |
| ----------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------- |
|Knowledge Question Answering | [TCM-ED-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-A.md) | 1,200    | Single-choice questions                                      | 12 subjects of the TCM intermediate attending physician examination | 100 questions are randomly selected for each subject         | Accuracy                                          |
|                               | [TCM-ED-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-B.md) | 4800     | Single-choice questions                                      | Practicing physician question bank                           | 8 complete practicing physician examination papers           | Accuracy                                          |
|                               | [TCM-FT](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FT.md) | 100      | Questions and Answers                                        | "Chinese Medicine Question and Answer Database" edited by Hu Ximing | 100 questions and answers are randomly selected from the question bank and reviewed by professionals | BertScore                                         |
| Language Understanding        | [TCMeEE](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCMeEE.md) | 100      | Based on medical records, entities related to Chinese medicine are identified and extracted to generate structured medical records. | The medical cases are from the website [《TCM Think Tank》](https://zhongyigen.com/) and real medical cases provided by Hunan University of Chinese Medicine | Use deepseek-r1 to generate answers, and then professionals review the generated answers | The average of BERTScore, ROUGE and BLEU is taken |
|                               | [TCM-CHGD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-CHGD.md) | 100      | Generate medical cases based on doctor-patient dialogues.    | Call deepseek r1 to generate doctor-patient dialogues based on real medical cases | 100 medical cases are used to reversely generate doctor-patient dialogues | The average of BERTScore, ROUGE and BLEU is taken |
|                               | [TCM-LitData](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-LitData.md) | 100      | Answer questions based on the content of the literature.     | [Dataset for TCM Literature Question Generation from Alibaba Cloud Tianchi Lab](https://tianchi.aliyun.com/dataset/86895) | 100 questions are randomly selected from the dataset and reviewed by professionals | Average of ROUGE and BLEU                         |
| Diagnosis                     | [TCM-MSDD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-MSDD.md) | 100      | Infer the corresponding syndrome type and disease name from clinical information. | [Alibaba Cloud Tianchi Lab CCL25-Eval Task 9 Dataset Subtask 1](https://tianchi.aliyun.com/competition/entrance/532301) | Randomly select 100 questions and have them reviewed by professionals | CCL25-Eval Task 9 task1_score                     |
|                               | [TCM-Diagnosis](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-Diagnosis.md) | 200      | Give the disease name, syndrome name, location, and nature of the disease based on the symptoms. | Real internal medicine, internal medicine, gynecology and pediatrics syndrome data set provided by Hunan University of Chinese Medicine | 50 cases are selected from each of the four subjects of internal medicine, internal medicine, gynecology and pediatrics | Average of BERTScore, ROUGE and BLEU              |
| Prescription recommendation   | [TCM-PR](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-PR.md) | 100      | Recommend appropriate Chinese medicine prescriptions based on clinical information. | [Alibaba Cloud Tianchi Laboratory CCL25-Eval Task 9 Dataset Subtask 2](https://tianchi.aliyun.com/competition/entrance/532301) | Randomly select 100 questions from the dataset and review them by professionals | CCL25-Eval Task 9 task2_score                     |
|                               | [TCM-FRD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FRD.md) | 200      | Give treatment methods, prescription names, and drug composition (excluding dosage) based on the manifestation of the syndrome. | Real internal medicine, internal medicine, gynecology and pediatric syndrome data set provided by Hunan University of Chinese Medicine | 200 cases of internal medicine, internal medicine, gynecology and pediatrics were selected | Average of BERTScore, ROUGE and BLEU              |
| Safety evaluation             | [TCM-SAFE1](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md) | 50       | Fill-in-the-blank questions                                  | Safety problem data set provided by Hunan University of Chinese Medicine | Common Chinese medicine and acupuncture contraindications fill-in-the-blank questions (50 questions) | LLM scoring                                       |
|                               | [TCM-SAFE2](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md) | 50       | Single-choice questions                                      | Safety problem data set provided by Hunan University of Chinese Medicine | Common contraindications of traditional Chinese medicine and acupuncture (single-choice questions) (50 questions) | Accuracy                                          |



## 🔆Submission and Evaluation Process

### Environment Configuration


Ensure that your development environment has installed the Python libraries required by the [requirements.txt file](https://github.com/Wayyuanyuan/MTCMB/blob/main/requirements.txt).


Currently, we provide an invocation template based on the OpenAI library, as well as three invocation templates for open-source libraries on Hugging Face: `HuatuoGPT-II`, `Taiyi-LLM`, and `WiNGPT2`. If you need support for additional invocations, please extend the `ChatInvoker` interface from the `make_answer/chat/chat_invoker.py` module.

#### OpenAI Library-Based Invocation Template

`module_name.call_llm`.py


```python
import os
import openai

from loguru import logger
from make_answer.chat.chat_invoker import ChatInvoker


class LlmOpenai(ChatInvoker):
    def __init__(self, *args, **kwargs):
        base_url = os.environ.get("OPENAI_BASE_URL")
        if "base_url" in kwargs:
            base_url = kwargs["base_url"]
        api_key = os.environ.get("OPENAI_API_KEY")
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        self.client = openai.OpenAI(
            base_url=base_url, api_key=api_key)
        self.model_name = kwargs["model_name"]

    def chat(self, msg: str, *args, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "你是一个专业中医医生，能够准确全面的解答中医问题。本次对话，均只采用中文提问和回答。"},
                {"role": "user", "content": msg}
            ]
        )
        try:
            ret = response.choices[0].message.content
        except Exception as e:
            logger.exception(f"call openai chat api error: {response}")
            raise e

        return ret
```

##### Usage

```python
python main.py \
--step-chat data/ \  # Folder containing the test questions
--api-model module_name.call_llm_file.ClassName \  # Custom test model, must inherit from ChatInvoker; provide the full module name, file name, and class name
--api-model-name large_model_name \  # Name of the large model being invoked, used to differentiate between different models and their results
--base-url model_api_url \  # URL for invoking the model
--api-key model_api_key  # API key for invoking the model
```

##### Example of Invocation Using the OpenAI Library

```
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your_key --num-process 12
```



#### Local Invocation Method

`module_name.call_llm`.py

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalLLM(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int = 0):
        # Model initialization, which is only performed on the first run.

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        # To request a response from the model, the msg parameter is required.
```

##### Usage Instructions

```python
python main.py \
--step-chat data/ \  # Directory containing the test questions
--local-model /Path/To/LLM \  # Directory where the local large language model (LLM) is located
--model-type LLM_name  # Name of the large language model; the custom template constructor must be written in `make_answer/chat/__init__.py` within the `name_model_dict`.
--prompt-type   # Set the prompt type, 0 represents zero-shot, 1 represents few-shot, 2 represents CoT'
```

##### Example

```
python main.py --step-chat data/ --local-model  /mnt/data1/MedLLM_baselines/Taiyi --model-type taiyi
```



## Submission Format Requirements



Our evaluation benchmark includes 11 datasets, each containing multiple questions with an empty 'answer' field. A brief example is provided below:

```
{"id":1,"question": "4.阴中求阳的治法适用于","options": ["A.阳盛","B.阴阳两虚","C.阴虚","D.阳虚","E.阴盛"],"answer": ""   }
{"id":2,"question": "15.精血同源是指","options": ["A.肝肾同源","B.心肾同源","C.脾胃同源","D.脾肾同源","E.心脾同源"],"answer": ""}
{"id":3,"question": "8.气虚证可见。","options": ["A.自汗","B.盗汗","C.半身出汗","D.战汗","E.头汗"],"answer": ""}
```

Our Evaluation Code Requires the Following Data Format

```
{"id":1,"question": "4.阴中求阳的治法适用于","options": ["A.阳盛","B.阴阳两虚","C.阴虚","D.阳虚","E.阴盛"],"answer": "D"   }
{"id":2,"question": "15.精血同源是指","options": ["A.肝肾同源","B.心肾同源","C.脾胃同源","D.脾肾同源","E.心脾同源"],"answer": "A"}
{"id":3,"question": "8.气虚证可见。","options": ["A.自汗","B.盗汗","C.半身出汗","D.战汗","E.头汗"],"answer": "A"}
```

Essentially, the 'answer' Field Is Populated with Model Responses. These responses are saved in a file named `mid.jsonl`.

Submission Naming Convention for 12 Datasets. We have 12 datasets, and we expect submissions to follow the naming convention outlined below:

```
Primary Directory (Model Name)
├── TCM-ED-A
│   └── mid.jsonl
├── TCM-ED-B
│   └── mid.jsonl
├── TCM-FT
│   └── mid.jsonl
├── TCMeEE
│   └── mid.jsonl
├── TCM-CHGD
│   └── mid.jsonl
├── TCM-LitData
│   └── mid.jsonl
├── TCM-MSDD
│   └── mid.jsonl
├── TCM-Diagnosis
│   └── mid.jsonl
├── TCM-PR
│   └── mid.jsonl
├── TCM-FRD
│   └── mid.jsonl
├── TCM-SAFE1
│   └── mid.jsonl
├── TCM-SAFE2
   └── mid.jsonl
```

Please submit your files in a compressed package, such as **gemini-1.5-pro.zip**, and send it to **weiyy53@mail2.sysu.edu.cn**. After the evaluation process is complete, the results will be published on **GitHub**.  

If you have any questions, feel free to contact us.
## Acknowledgments

We sincerely thank all organizations and individuals who have provided support and assistance to this project. 🎉🎉🎉  

We also extend our heartfelt gratitude to all team members who contributed to this project!

