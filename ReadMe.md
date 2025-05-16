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

（2）[Huggingface datasets](https://huggingface.co/datasets/Bunnybeck/MTCMB/tree/main)



## 📍Ranking List
 
#### 🔆Universal LLMs

#### 

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.SE-A   | 12.SE-B |
| -------------------- | ---------- | ---------- | --------- | -------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | ------- |
| gpt-4.1              | 64.67      | 75.15      | 86.62     | 52       | 55         | 64            | 35         | 49              | 35       | 49         | 70.99     | 74      |
| gpt-4.1 Few-Shot     | 72.01      | 74.25      | 86.77     | 78       | 48         | 59            | 34.44      | 51              | 40       | 54         | 73.15     | 72.34   |
| gpt-4.1 CoT          | 73.02      | 72.05      | 88.17     | 72       | 47         | 64            | 35.46      | 51              | 40       | 54         | 72.76     | 68.09   |
| claude               | 59.42      | 59.58      | 85.93     | 69       | 50         | 56            | 12.75      | 39              | 31       | 36         | 58.76     | 48      |
| claude Few-Shot      | 64.24      | 62.96      | 87.58     | 79       | 51         | 55            | 38.52      | 44              | 38       | 38         | 64.94     | 55.32   |
| claude CoT           | 63.99      | 51.68      | 87.97     | 54       | 43         | 57            | 30.87      | 41              | 34       | 39         | 48.83     | 53.19   |
| gemini               | 83.5       | 86.6       | 88.33     | 77       | 46         | 65            | 32.25      | 46              | 37       | 39         | 82.04     | 86      |
| gemini Few-Shot      | 85.05      | 87.22      | 89.18     | 75       | 48         | 57            | 35.71      | 47              | 40       | 50         | 82.37     | 87.23   |
| gemini CoT           | 85.71      | 66.69      | 87.37     | 79       | 47         | 62            | 34.95      | 47              | 38       | 50         | 77.8      | 85.11   |
| qwen-max             | 86.92      | 90.54      | 87.43     | 51       | 50         | 68            | 30         | 49              | 36       | 44         | 77.16     | 78      |
| qwen-max Few-Shot    | 88.14      | 90.43      | 88.10     | 80       | 50         | 65            | 40.05      | 52              | 40       | 54         | 79.11     | 82.98   |
| qwen-max CoT         | 86.72      | 75.42      | 88.01     | 51       | 49         | **71**        | 38.01      | **53**          | 40       | 54         | 77.83     | 80.85   |
| glm-4-plus           | 83.83      | 87.25      | 87.67     | 82       | 47         | 64            | 32.5       | 46              | 37       | 38         | 72.73     | 74      |
| glm-4-plus Few-Shot  | 82.54      | 86.64      | 88.19     | 80       | 49         | 62            | 40.05      | 47              | 40       | 51         | 78.26     | 74.47   |
| glm-4-plus CoT       | 82.04      | 80.53      | 88.07     | 82       | 48         | 63            | 37.24      | 34              | **41**   | 50         | 78.96     | 74.47   |
| doubao               | **92.08**  | **94.21**  | 89.22     | 86       | 46         | 67            | 33.75      | 50              | 37       | 52         | 83.16     | **90**  |
| doubao Few-Shot      | 91.48      | 94.04      | 89.22     | 83       | **56**     | 62            | 39.54      | 51              | 39       | **58**     | 83.18     | 87.23   |
| doubao CoT           | 91.73      | 83.97      | **89.59** | 86       | 50         | 34            | 37.5       | 51              | 39       | 54         | 81.17     | 85.11   |
| DeepSeek-V3          | 89.08      | 91.17      | 87.66     | **87**   | 48         | 62            | 39.25      | 50              | 39       | 41         | **85.86** | 82      |
| DeepSeek-V3 Few-Shot | 89.64      | 90.95      | 88.30     | 83       | 52         | 61            | **41.33**  | 51              | 40       | 56         | 85.25     | 80.85   |
| DeepSeek-V3 CoT      | 88.47      | 80.11      | 88.65     | 86       | 51         | 62            | 38.78      | 51              | 40       | 54         | 81.02     | 74.47   |




####  🔆Reasoning LLMs

#### 

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.SE-A   | 12.SE-B   |
| -------------------- | ---------- | ---------- | --------- | -------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | --------- |
| o4-mini              | 70.92      | 74.42      | 86.88     | 78       | 45         | 61            | 17.25      | 51              | 26       | 43         | 55.3      | 54        |
| o4-mini Few-Shot     | 69.92      | 74.34      | 86.21     | 79       | 47         | **64**        | 28.06      | **52**          | 38       | 52         | 58.55     | 70.21     |
| qwen3-235B           | 86.83      | 91.54      | **88.29** | 53       | **58**     | 60            | 42         | 49              | 35       | 46         | 71.36     | 86        |
| qwen3-235B Few-Shot  | 87.13      | 89.58      | 87.51     | 79       | 50         | 60            | **50**     | 50              | 40       | **54**     | 70.32     | 80.85     |
| DeepSeek-r1          | 89.08      | 91.17      | 87.66     | **87**   | 48         | 62            | 39.25      | 50              | 39       | 41         | **85.86** | 82        |
| DeepSeek-r1 Few-Shot | **92.40**  | **92.33**  | 84.21     | 83       | 52         | 61            | 40.05      | 49              | **41**   | 52         | 86.26     | **89.36** |





#### 

####  🔆Medical professional LLMs

#### 

| Model            | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCM-eEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.SE-A   | 12.SE-B |
| ---------------- | ---------- | ---------- | --------- | --------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | ------- |
| WINGPT2-14B-Chat | 40.25      | 40.98      | 84.42     | 57        | 40         | 44            | 17         | 45              | 22       | 35         | 43.2      | 46      |
| WINGPT2-14B-Chat Few-Shot         | 41         | 44.9       | 85.13     | 69        | 44         | 38            | 23         | 48              | 21       | **43**     | 39.38     | 44      |
| WINGPT2-14B-Chat CoT              | 42.08      | 41.88      | 84.66     | 52        | 42         | 36            | 16.75      | 47              | 19       | 30         | 43.1      | 32      |
| TaiYi-LLM        | 39.92      | 47.71      | 82.82     | 49        | 29         | **61**        | 13.5       | 49              | 11       | 30         | 24.07     | 28      |
| TaiYi-LLM Few-Shot         | 39.67      | 42.94      | 80.18     | 55        | 25         | 43            | 35.5       | 48              | 19       | 29         | 28.13     | 40      |
| TaiYi-LLM CoT              | 39.17      | 39.54      | 78.83     | 32        | 32         | 47            | 31.75      | 35              | 10       | 29         | 25.73     | 30      |
| DISC-MedLLM      | 31.33      | 32.42      | 80.34     | 45        | 34         | 19            | 3          | 44              | 19       | 26         | 35        | 0       |
| DISC-MedLLM  Few-Shot         | 27.17      | 29.31      | 82.88     | 31        | 28         | 22            | 1.5        | 38              | 17       | 32         | 37.42     | 2       |
| DISC-MedLLM CoT              | 26.58      | 31.42      | 83.45     | 24        | 23         | 24            | 4          | 37              | 7        | 25         | 42.52     | 0       |
| HuatuoGPT-o1-72b | 75.17      | **82.27**  | 86.32     | 82        | 45         | 40            | 20.25      | 45              | 24       | **45**     | 51.3      | 70      |
| HuatuoGPT-o1-72b Few-Shot         | 73         | 81.13      | 86.91     | 80        | **48**     | 44            | 34.25      | 41              | 32       | 34         | 52.2      | 68      |
| HuatuoGPT-o1-72b CoT              | 72         | 79.13      | 86.86     | 82        | **48**     | 43            | 30         | 42              | 26       | 35         | 58.65     | 70      |
| Baichuan-14b-M1  | 79.83      | 82.02      | **87.49** | 82        | 46         | **63**        | 35.5       | 46              | 33       | 38         | 70.36     | 66      |
| Baichuan-14b-M1 Few-Shot         | 28.5       | 80.88      | 87.31     | 80        | 42         | 57            | **46.75**  | **51**          | **38**   | 32         | 73.36     | **72**  |
| Baichuan-14b-M1 CoT              | **85.08**  | 55.81      | 87.07     | **84**    | 44         | 34            | 36.5       | **51**          | 37       | 20         | **76.09** | 68      |

## 😊Dataset Description


#### **Data Structure**

Dataset: **5** Dimensions, **12** Datasets

The following figure shows the data volume distribution in four dimensions: language understanding, diagnosis, prescription recommendation, and safety assessment:

![pie-nest](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/line-simple-en.png)

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
|Knowledge Question Answering | [TCM-ED-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-A.md) | 1,200    | Multiple-choice questions                                     | 12 subjects of the TCM intermediate attending physician examination | 100 questions are randomly selected for each subject         | Accuracy                                          |
|                               | [TCM-ED-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-B.md) | 4800     | Multiple-choice questions                                     | Practicing physician question bank                           | 8 complete practicing physician examination papers           | Accuracy                                          |
|                               | [TCM-FT](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FT.md) | 100      | Questions and Answers                                        | "Chinese Medicine Question and Answer Database" edited by Hu Ximing | 100 questions and answers are randomly selected from the question bank and reviewed by professionals | BertScore                                         |
| Language Understanding        | [TCMeEE](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCMeEE.md) | 100      | Based on medical records, entities related to Chinese medicine are identified and extracted to generate structured medical records. | The medical cases are from the website [《TCM Think Tank》](https://zhongyigen.com/) and real medical cases provided by Hunan University of Chinese Medicine | Use deepseek-r1 to generate answers, and then professionals review the generated answers | The average of BERTScore, ROUGE and BLEU is taken |
|                               | [TCM-CHGD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-CHGD.md) | 100      | Generate medical cases based on doctor-patient dialogues.    | Call deepseek r1 to generate doctor-patient dialogues based on real medical cases | 100 medical cases are used to reversely generate doctor-patient dialogues | The average of BERTScore, ROUGE and BLEU is taken |
|                               | [TCM-LitData](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-LitData.md) | 100      | Answer questions based on the content of the literature.     | [Dataset for TCM Literature Question Generation from Alibaba Cloud Tianchi Lab](https://tianchi.aliyun.com/dataset/86895) | 100 questions are randomly selected from the dataset and reviewed by professionals | Average of ROUGE and BLEU                         |
| Diagnosis                     | [TCM-MSDD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-MSDD.md) | 100      | Infer the corresponding syndrome type and disease name from clinical information. | [Alibaba Cloud Tianchi Lab CCL25-Eval Task 9 Dataset Subtask 1](https://tianchi.aliyun.com/competition/entrance/532301) | Randomly select 100 questions and have them reviewed by professionals | CCL25-Eval Task 9 task1_score                     |
|                               | [TCM-Diagnosis](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-Diagnosis.md) | 200      | Give the disease name, syndrome name, location, and nature of the disease based on the symptoms. | Real internal medicine, internal medicine, gynecology and pediatrics syndrome data set provided by Hunan University of Chinese Medicine | 50 cases are selected from each of the four subjects of internal medicine, internal medicine, gynecology and pediatrics | Average of BERTScore, ROUGE and BLEU              |
| Prescription recommendation   | [TCM-PR](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-PR.md) | 100      | Recommend appropriate Chinese medicine prescriptions based on clinical information. | [Alibaba Cloud Tianchi Laboratory CCL25-Eval Task 9 Dataset Subtask 2](https://tianchi.aliyun.com/competition/entrance/532301) | Randomly select 100 questions from the dataset and review them by professionals | CCL25-Eval Task 9 task2_score                     |
|                               | [TCM-FRD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FRD.md) | 200      | Give treatment methods, prescription names, and drug composition (excluding dosage) based on the manifestation of the syndrome. | Real internal medicine, internal medicine, gynecology and pediatric syndrome data set provided by Hunan University of Chinese Medicine | 200 cases of internal medicine, internal medicine, gynecology and pediatrics were selected | Average of BERTScore, ROUGE and BLEU              |
| Safety evaluation             | [SE-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md) | 50       | Fill-in-the-blank questions                                  | Safety problem data set provided by Hunan University of Chinese Medicine | Common Chinese medicine and acupuncture contraindications fill-in-the-blank questions (50 questions) | LLM scoring                                       |
|                               | [SE-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md) | 50       | Multiple-choice questions                                     | Safety problem data set provided by Hunan University of Chinese Medicine | Common contraindications of traditional Chinese medicine and acupuncture (multiple-choice questions) (50 questions) | Accuracy                                          |



## 🔆Submission and Evaluation Process


### Environment Configuration


Ensure that your development environment has installed the Python libraries required by the [requirements.txt file](https://github.com/Wayyuanyuan/MTCMB/blob/main/requirements.txt).

### Answer Module

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
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your_key --num-process 12 --prompt-type   # Set the prompt type, 0 represents zero-shot, 1 represents few-shot, 2 represents CoT'
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
### Evaluation Module

**Usage**

```python
python main.py \
--step-evaluate LLM Answers Directory \ # Typically, pass the model name under the root directory
--standard-answer-root Standard answer directory # Pass the directory containing standard answers
```

### Other Parameters

| Parameter Name  | Default Value | Description                                                  |
| --------------- | ------------- | ------------------------------------------------------------ |
| `--num-process` | 1             | Number of concurrent threads when calling the large language model for responses and evaluations |
| `--sleep-time`  | 0             | Waiting time after each response from the large model        |




## Submission Format Requirements



Our evaluation benchmark includes 11 datasets, each containing multiple questions with an empty 'answer' field. A brief example is provided below:

```
{"id": 1,"question": "4.‘Formulas that seek yang within yin’ is applicable to?","options": ["A.Yang excess","B.Dual deficiency of yin and yang","C.Yin deficiency","D.Yang deficiency","E.Yin excess"],"answer": ""}
{"id": 2,"question": "15.What does ‘Essence and blood share the same source’ refer to? ","options": ["A.Liver and kidney share the same source","B.Heart and kidney share the same source","C.Spleen and stomach share the same source","D.Spleen and kidney share the same source","E.Heart and spleen share the same source"],"answer": ""}
{"id":3,"question": "8.The symptoms of Qi deficiency pattern include。","options": ["A.Spontaneous sweating","B.Night sweats","C.Hemilateral sweating","D.Sweating after shivering","E.Head sweating"],"answer": ""}
```

Our Evaluation Code Requires the Following Data Format

```
{"id": 1,"question": "4.‘Formulas that seek yang within yin’ is applicable to?","options": ["A.Yang excess","B.Dual deficiency of yin and yang","C.Yin deficiency","D.Yang deficiency","E.Yin excess"],"answer": "D"}
{"id": 2,"question": "15.What does ‘Essence and blood share the same source’ refer to? ","options": ["A.Liver and kidney share the same source","B.Heart and kidney share the same source","C.Spleen and stomach share the same source","D.Spleen and kidney share the same source","E.Heart and spleen share the same source"],"answer": "A"}
{"id":3,"question": "8.The symptoms of Qi deficiency pattern include。","options": ["A.Spontaneous sweating","B.Night sweats","C.Hemilateral sweating","D.Sweating after shivering","E.Head sweating"],"answer": "A"}
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
├── SE-A
│   └── mid.jsonl
├── SE-B
   └── mid.jsonl
```

Please submit your files in a compressed package, such as **gemini-1.5-pro.zip**, and send it to **weiyy53@mail2.sysu.edu.cn**. After the evaluation process is complete, the results will be published on **GitHub**.  

If you have any questions, feel free to contact us.
## Acknowledgments

We sincerely thank all organizations and individuals who have provided support and assistance to this project. 🎉🎉🎉  

We also extend our heartfelt gratitude to all team members who contributed to this project!

