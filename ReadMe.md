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
Min-Max Normalized Score (MMN Score)
 
#### 🔆Universal LLMs

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | MMN Score | 5.TCM-CHGD | MMN Score | 6.TCM-LitData | MMN Score | 7.TCM-MSDD | 8.TCM-DiagData | MMN Score | 9.TCM-PR | 10.TCM-FRD | MMN Score | 11.TCM-DC-A | 12.TCM-DC-B |
| -------------------- | ---------- | ---------- | --------- | -------- | --------- | ---------- | --------- | ------------- | --------- | ---------- | -------------- | --------- | -------- | ---------- | --------- | ----------- | ----------- |
| gpt-4.1              | 64.67      | 75.15      | 86.62     | 52       | 38.14     | 55         | 53.83     | 64            | 59.73     | 35         | 49             | 45.74     | 35       | 49         | 51.44     | 70.99       | 74          |
| gpt-4.1 Few-Shot     | 72.01      | 74.25      | 86.77     | 78       | 57.84     | 48         | 50.63     | 59            | 62.52     | 34.44      | 51             | 46.76     | 40       | 54         | 51.43     | 73.15       | 72.34       |
| gpt-4.1 CoT          | 73.02      | 72.05      | 88.17     | 72       | 63.69     | 47         | 53.17     | 64            | 64.98     | 35.46      | 51             | 42.71     | 40       | 54         | 50.75     | 72.76       | 68.09       |
| claude               | 59.42      | 59.58      | 85.93     | 69       | 61.01     | 50         | 43.66     | 56            | 56.11     | 12.75      | 39             | 54.12     | 31       | 36         | 39.3      | 58.76       | 48          |
| claude Few-Shot      | 64.24      | 62.96      | 87.58     | 79       | 48.27     | 51         | 53.58     | 55            | 51.79     | 38.52      | 44             | 43.81     | 38       | 38         | 34.99     | 64.94       | 55.32       |
| claude CoT           | 63.99      | 51.68      | 87.97     | 54       | 44.09     | 43         | 37.46     | 57            | 53.7      | 30.87      | 41             | 48.67     | 34       | 39         | 37.96     | 48.83       | 53.19       |
| gemini               | 83.5       | 86.6       | 88.33     | 77       | 52.83     | 46         | 50.01     | 65            | 63.19     | 32.25      | 46             | 41.56     | 37       | 39         | 31.58     | 82.04       | 86          |
| gemini Few-Shot      | 85.05      | 87.22      | 89.18     | 75       | 58.56     | 48         | 47.23     | 57            | 60.35     | 35.71      | 47             | 44.83     | 40       | 50         | 55.76     | 82.37       | 87.23       |
| gemini CoT           | 85.71      | 66.69      | 87.37     | 79       | 59.63     | 47         | 53.36     | 62            | 59.36     | 34.95      | 47             | 44.51     | 38       | 50         | 53.38     | 77.8        | 85.11       |
| qwen-max             | 86.92      | 90.54      | 87.43     | 51       | 49.07     | 50         | 43.27     | 68            | 62.22     | 30         | 49             | 37.02     | 36       | 44         | 39.88     | 77.16       | 78          |
| qwen-max Few-Shot    | 88.14      | 90.43      | 88.10     | 80       | 61.04     | 50         | 52.3      | 65            | 63.34     | 40.05      | 52             | 50.44     | 40       | 54         | 49.24     | 79.11       | 82.98       |
| qwen-max CoT         | 86.72      | 75.42      | 88.01     | 51       | 47.64     | 49         | 54.54     | **71**        | **66.17** | 38.01      | **53**         | 53.74     | 40       | 54         | **63.17** | 77.83       | 80.85       |
| glm-4-plus           | 83.83      | 87.25      | 87.67     | 82       | 56.48     | 47         | 50.75     | 64            | 58.18     | 32.5       | 46             | 40.86     | 37       | 38         | 39.34     | 72.73       | 74          |
| glm-4-plus Few-Shot  | 82.54      | 86.64      | 88.19     | 80       | 61.58     | 49         | 49.54     | 62            | 56.16     | 40.05      | 47             | 44.67     | 40       | 51         | 55.04     | 78.26       | 74.47       |
| glm-4-plus CoT       | 82.04      | 80.53      | 88.07     | 82       | 64.52     | 48         | 51.34     | 63            | 58.13     | 37.24      | 34             | 28.13     | **41**   | 50         | 63.83     | 78.96       | 74.47       |
| doubao               | **92.08**  | **94.21**  | 89.22     | 86       | 64.29     | 46         | **55.69** | 67            | 61.3      | 33.75      | 50             | 54.22     | 37       | 52         | 49.14     | 83.16       | **90**      |
| doubao Few-Shot      | 91.48      | 94.04      | 89.22     | 83       | 65.79     | **56**     | 53.63     | 62            | 58.17     | 39.54      | 51             | 51.71     | 39       | **58**     | 57.18     | 83.18       | 87.23       |
| doubao CoT           | 91.73      | 83.97      | **89.59** | 86       | 65.8      | 50         | 51.05     | 34            | 52.06     | 37.5       | 51             | **63.57** | 39       | 54         | 57.85     | 81.17       | 85.11       |
| DeepSeek-V3          | 89.08      | 91.17      | 87.66     | **87**   | 65.9      | 48         | 52.19     | 62            | 56.46     | 39.25      | 50             | 44.81     | 39       | 41         | 31.43     | **85.86**   | 82          |
| DeepSeek-V3 Few-Shot | 89.64      | 90.95      | 88.30     | 83       | 55.25     | 52         | 51.64     | 61            | 55.27     | **41.33**  | 51             | 49.73     | 40       | 56         | 48.62     | 85.25       | 80.85       |
| DeepSeek-V3 CoT      | 88.47      | 80.11      | 88.65     | 86       | **66.62** | 51         | 51.73     | 62            | 55.61     | 38.78      | 51             | 46.85     | 40       | 54         | 49.37     | 81.02       | 74.47       |




####  🔆Reasoning LLMs

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | MMN Score | 5.TCM-CHGD | MMN Score | 6.TCM-LitData | MMN Score | 7.TCM-MSDD | 8.TCM-DiagData | MMN Score | 9.TCM-PR | 10.TCM-FRD | MMN Score | 11.TCM-DC-A | 12.TCM-DC-B |
| -------------------- | ---------- | ---------- | --------- | -------- | --------- | ---------- | --------- | ------------- | --------- | ---------- | -------------- | --------- | -------- | ---------- | --------- | ----------- | ----------- |
| o4-mini              | 70.92      | 74.42      | 86.88     | 78       | 54.82     | 45         | 52.47     | 61            | 59.3      | 17.25      | 51             | **47.4**  | 26       | 43         | 39.95     | 55.3        | 54          |
| o4-mini Few-Shot     | 69.92      | 74.34      | 86.21     | 79       | 58.05     | 47         | 49.62     | **64**        | 61.78     | 28.06      | **52**         | 44.84     | 38       | 52         | 41.01     | 58.55       | 70.21       |
| qwen3-235B           | 86.83      | 91.54      | **88.29** | 53       | 37.28     | **58**     | **56.72** | 60            | 53.62     | 42         | 49             | 44.15     | 35       | 46         | 40.25     | 71.36       | 86          |
| qwen3-235B Few-Shot  | 87.13      | 89.58      | 87.51     | 79       | 58.67     | 50         | 51.76     | 60            | **61.46** | **50**     | 50             | 47.08     | 40       | **54**     | 46.97     | 70.32       | 80.85       |
| DeepSeek-r1          | 89.08      | 91.17      | 87.66     | **87**   | 59.32     | 48         | 49.17     | 62            | 51.11     | 39.25      | 50             | 40.3      | 39       | 41         | 44.62     | **85.86**   | 82          |
| DeepSeek-r1 Few-Shot | **92.40**  | **92.33**  | 84.21     | 83       | **61.29** | 52         | 55.38     | 61            | 64.81     | 40.05      | 49             | 36.39     | **41**   | 52         | **51.35** | 86.26       | **89.36**   |




####  🔆Medical professional LLMs

| Model            | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCM-eEE | MMN Score | 5.TCM-CHGD | MMN Score | 6.TCM-LitData | MMN Score | 7.TCM-MSDD | 8.TCM-DiagData | MMN Score | 9.TCM-PR | 10.TCM-FRD | MMN Score | 11.TCM-DC-A | 12.TCM-DC-B |
| ---------------- | ---------- | ---------- | --------- | --------- | --------- | ---------- | --------- | ------------- | --------- | ---------- | -------------- | --------- | -------- | ---------- | --------- | ----------- | ----------- |
| WINGPT2-14B-Chat | 40.25      | 40.98      | 84.42     | 57        | 57.54     | 40         | 43.78     | 44            | 44.47     | 17         | 45             | 44.24     | 22       | 35         | 38.74     | 43.2        | 46          |
| Few-Shot         | 41         | 44.9       | 85.13     | 69        | 61.75     | 44         | 40.36     | 38            | 38.17     | 23         | 48             | 56.65     | 21       | **43**     | **46.85** | 39.38       | 44          |
| CoT              | 42.08      | 41.88      | 84.66     | 52        | 53.64     | 42         | **45.69** | 36            | 38.18     | 16.75      | 47             | 55.18     | 19       | 30         | 24.41     | 43.1        | 32          |
| TaiYi-LLM        | 39.92      | 47.71      | 82.82     | 49        | 55.26     | 29         | 29.02     | **61**        | 59.62     | 13.5       | 49             | **73.74** | 11       | 30         | 34.09     | 24.07       | 28          |
| Few-Shot         | 39.67      | 42.94      | 80.18     | 55        | **63.09** | 25         | 36.07     | 43            | 46.65     | 35.5       | 48             | 55.96     | 19       | 29         | 28.49     | 28.13       | 40          |
| CoT              | 39.17      | 39.54      | 78.83     | 32        | 31.63     | 32         | 30.56     | 47            | 49.4      | 31.75      | 35             | 41.5      | 10       | 29         | 36.62     | 25.73       | 30          |
| DISC-MedLLM      | 31.33      | 32.42      | 80.34     | 45        | 50.06     | 34         | 33.67     | 19            | 24.5      | 3          | 44             | 71.75     | 19       | 26         | 25.02     | 35          | 0           |
| Few-Shot         | 27.17      | 29.31      | 82.88     | 31        | 25.99     | 28         | 26.34     | 22            | 22.58     | 1.5        | 38             | 48.04     | 17       | 32         | 32.46     | 37.42       | 2           |
| CoT              | 26.58      | 31.42      | 83.45     | 24        | 15.7      | 23         | 35.36     | 24            | 27.9      | 4          | 37             | 48.7      | 7        | 25         | 22.78     | 42.52       | 0           |
| HuatuoGPT-o1-72b | 75.17      | **82.27**  | 86.32     | 82        | 63.87     | 45         | 52.6      | 40            | 38.81     | 20.25      | 45             | 35.02     | 24       | **45**     | 49.29     | 51.3        | 70          |
| Few-Shot         | 73         | 81.13      | 86.91     | 80        | 50.11     | **48**     | 32.16     | 44            | 35.99     | 34.25      | 41             | 43.66     | 32       | 34         | 20.4      | 52.2        | 68          |
| cot              | 72         | 79.13      | 86.86     | 82        | **75.71** | **48**     | 35.41     | 43            | 36.5      | 30         | 42             | 44.64     | 26       | 35         | 22.29     | 58.65       | 70          |
| Baichuan-14b-M1  | 79.83      | 82.02      | **87.49** | 82        | 57.29     | 46         | 44.39     | **63**        | **61.05** | 35.5       | 46             | 37.05     | 33       | 38         | 30.92     | 70.36       | 66          |
| Few-Shot         | 28.5       | 80.88      | 87.31     | 80        | 55.46     | 42         | 38.03     | 57            | 57.64     | **46.75**  | **51**         | 46.05     | **38**   | 32         | 28.44     | 73.36       | **72**      |
| cot              | **85.08**  | 55.81      | 87.07     | **84**    | 49.59     | 44         | 43.36     | 34            | 46.06     | 36.5       | **51**         | 45.36     | 37       | 20         | 3.72      | **76.09**   | 68          |

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

