# MTCMB 多任务中医评估基准 

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>


![title](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/title2.png)

<p align="center">
   📃 <a href="" target="_blank">Paper</a> • 🌐 <a href="" target="_blank">Website</a>  
   <br>  <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe_cn.md">   中文</a> | <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe.md"> English
</p>


## 🌈 更新

- **[2025.5.15]** 发布了论文。
- **[2025.5.15]** 🎉🎉🎉 MTCMB 正式发布！🎉🎉🎉

## 🌐 数据下载

（1）Zip格式

```python
  https://github.com/Wayyuanyuan/MTCMB.git && cd data
```

（2）[百度云链接]( https://pan.baidu.com/s/1_pOlvjRNEbOp29oDPi7bRQ?pwd=vgzt)

## 📍排行榜​​

## 😊数据集描述

#### 结构

数据集：**5**个维度，**12**个数据集

语言理解、诊断、方剂推荐、安全评价**4个维度**的数据量分布如下图所示

![pie-nest](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/area-stack%20-ch.png)

🥸 **知识问答**维度包含三个数据集，分别是TCM-ED-A（1200）、TCM-ED-B（4800）、TCM-FT（100）



- **知识问答**：通过中级主治医师和执业医师考试题目以及标准问答题形式，考察大模型对中医基础理论、方剂学、针灸学、诊断学等核心知识的理解与应用能力。

- **语言理解**：通过医案中的实体抽取、从医患对话生成结构化医案以及基于文献内容回答问题等形式，评估大模型在中医文本理解和信息抽取方面的表现力与准确性。

- **诊断**：考察大模型根据患者临床信息（如症状、体征、舌脉等）进行辨证分析，并准确判断疾病名称与证型的能力。

- **方剂推荐**：评估大模型根据病情描述和证型特征，推荐合适中药方剂的能力，涵盖对方剂组成、配伍规律及病症对应关系的理解。

- **安全评价**：通过填空题与选择题的形式，考察大模型识别中医实践中涉及的安全风险，如有毒中药剂量控制、孕妇禁用药及针灸禁忌等内容，确保其具备基本的临床安全性判断能力。

  

#### 详细信息

**点击超链接可以查看到不同数据集格式要求**⬅️⬅️

| 维度         | 数据集名称    | 数量  | 任务描述                                               | 数据来源                                                     | 构建方式                                      | 评估方法                           |
| ------------ | ------------- | ----- | ------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------- | ---------------------------------- |
| 中医知识问答 | [TCM-ED-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-A.md)      | 1,200 | 单项选择题                                             | 中医中级主治医师考试的12个学科                               | 每个学科随机抽取100道题目                     | 准确率                             |
|              | [TCM-ED-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-B.md)     | 4800  | 单项选择题                                             | 执业医师题库                                                 | 8份完整的执业医师试卷                         | 准确率                             |
|              | [TCM-FT](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FT.md)       | 100   | 问答题                                                 | 《中医学问答题库》胡熙明主编                                 | 从题库中随机抽取100道问答题，并由专业人员审核 | BertScore                          |
| 中医语言理解 | [TCMeEE](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCMeEE.md)        | 100   | 根据医案识别并抽取与中医相关的实体，生成结构化病历。   | 医案来源于[《中医智库》](https://zhongyigen.com/)网站及湖南中医药大学提供的真实医案 | 使用deepseek-r1模型生成答案后，由专业人员复核 | BERTScore、ROUGE 和 BLEU三者取平均 |
|              | [TCM-CHGD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-CHGD.md)      | 100   | 根据医患对话生成医案。                                 | 调用deepseek r1基于真实医案生成医患对话                      | 100份医案逆向生成医患对话                     | BERTScore、ROUGE 和 BLEU三者取平均 |
|              | [TCM-LitData](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-LitData.md)   | 100   | 根据文献内容回答问题。                                 | [阿里云天池实验室的中医文献问题生成数据集](https://tianchi.aliyun.com/dataset/86895) | 从数据集随机抽取100道题目，并且由专业人员复核 | ROUGE 和 BLEU二者取平均            |
| 中医诊断     | [TCM-MSDD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-MSDD.md)      | 100   | 从临床信息推断对应的证型和疾病名称。                   | [阿里云天池实验室CCL25-Eval任务9数据集子任务1](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-MSDD)             | 随机抽取100道并且由专业人员复核               | CCL25-Eval 任务9的task1_score      |
|              | [TCM-Diagnosis](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-Diagnosis.md) | 200   | 根据症状表现给出疾病名称、证名、病位、病性。           | 湖南中医药大学提供的真实内外妇儿证型数据集                   | 按照内外妇儿四个科目每科抽取50例              | BERTScore、ROUGE 和 BLEU三者取平均 |
| 方剂推荐     | [TCM-PR](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-PR.md)        | 100   | 根据临床信息推荐合适的中药处方。                       | [阿里云天池实验室CCL25-Eval任务9数据集子任务2]()             | 从数据集随机抽取100道题目，并且由专业人员复核 | CCL25-Eval 任务9的task2_score      |
|              | [TCM-FRD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FRD.md)       | 200   | 根据证的表现给出治法、方剂名、药物组成（不包含剂量）。 | 湖南中医药大学提供的真实内外妇儿证型数据集                   | 内外妇儿共抽取200例                           | BERTScore、ROUGE 和 BLEU三者取平均 |
| 中医安全评价 | [TCM-SAFE1](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md)     | 50    | 填空题                                                 | 湖南中医药大学提供的安全性问题数据集                         | 常见中药及针灸禁忌填空题（50题）              | 大模型评分                         |
|              | [TCM-SAFE2](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SAFE1%262.md)     | 50    | 选择题                                                 | 湖南中医药大学提供的安全性问题数据集                         | 常见中药及针灸禁忌选择题（50题）              | 准确率                             |



## 🔆如何提交和评估

### 环境配置


确保你的开发环境已经安装了[文件](https://github.com/Wayyuanyuan/MTCMB/blob/main/requirements.txt)要求的Python库


目前提供基于OpenAI库的调用模版，并且提供三套HuggingFace上开源库的调用模版，分别是`HuatuoGPT-II`，`Taiyi-LLM`和`WiNGPT2`调用。如果需要其他更多调用的支持，请继承自`make_answer/chat/chat_invoker.py`模块中的`ChatInvoker`接口。

#### 基于OpenAI库的调用模版

`模块名.调用llm文件`.py


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

##### 使用方式

```python
python main.py \
--step-chat data/ \ # 测试问题所在文件夹
--api-model 模块名.调用llm文件.类名 \ # 自定义测试模型，需要继承自ChatInvoker，传入完整模块名、文件名和类名
--api-model-name 调用的大模型名称 \ # 大模型名称，用于区分调用的不同模型，以及不同模型结果
--base-url 模型调用url \ # 模型url
--api-key 模型key  # 调用模型key
```

##### 基于OpenAI库的调用示例

```
python main.py --step-chat data --api-model make_answer.chat.remote.openai_api.LlmOpenai --llm-name your_model_name  --base-url your_url --api-key your_key --num-process 12 --prompt-type 0/1/2  #设置提示词类型，0代表zero-shot,1代表few-shot,2代表CoT'
```



#### 基于本地调用形式

`模块名.调用llm文件`.py

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from make_answer.chat.chat_invoker import ChatInvoker


class LocalLLM(ChatInvoker):
    def __init__(self, model_path: str, gpu_id: int = 0):
        # 模型初始化，仅在首次运行时执行。

    def chat(
            self, msg: str, *args, **kwargs
    ) -> str:
        # 请求模型回答，msg为必填参数。
```

##### 使用方式

```python
python main.py \
--step-chat data/ \ # 测试问题所在文件夹
--local-model /Path/To/LLM \ # 本地大模型所在目录
--model-type LLM名称 # 大模型名称，需要将自定模版构造函数写在：make_answer/chat/__init__.py的name_model_dict中。
--prompt-type 0/1/2  #设置提示词类型，0代表zero-shot,1代表few-shot,2代表CoT'
```

##### 一个示例

```
python main.py --step-chat data/ --local-model  /mnt/data1/MedLLM_baselines/Taiyi --model-type taiyi
```



## 提交格式要求



我们的评估基准包括11个数据集，每个数据集包含若干个题目，这些题目的answer字段为空。一个简短的示例如下：

```
{"id":1,"question": "4.阴中求阳的治法适用于","options": ["A.阳盛","B.阴阳两虚","C.阴虚","D.阳虚","E.阴盛"],"answer": ""   }
{"id":2,"question": "15.精血同源是指","options": ["A.肝肾同源","B.心肾同源","C.脾胃同源","D.脾肾同源","E.心脾同源"],"answer": ""}
{"id":3,"question": "8.气虚证可见。","options": ["A.自汗","B.盗汗","C.半身出汗","D.战汗","E.头汗"],"answer": ""}
```

我们的评估代码要求接受下面的数据格式，

```
{"id":1,"question": "4.阴中求阳的治法适用于","options": ["A.阳盛","B.阴阳两虚","C.阴虚","D.阳虚","E.阴盛"],"answer": "D"   }
{"id":2,"question": "15.精血同源是指","options": ["A.肝肾同源","B.心肾同源","C.脾胃同源","D.脾肾同源","E.心脾同源"],"answer": "A"}
{"id":3,"question": "8.气虚证可见。","options": ["A.自汗","B.盗汗","C.半身出汗","D.战汗","E.头汗"],"answer": "A"}
```

本质上是将answer字段使用模型的回答进行填充。这些的数据被保存在mid.jsonl文件中。

我们拥有12个数据集，我们期待采用以下的命名方式提交

```
一级目录 （模型名）
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

请将文件以压缩包形式提交，例如 **gemini-1.5-pro.zip**。压缩包请发送至邮箱 **weiyy53@mail2.sysu.edu.cn**。
我们将在评估完成后，于 **GitHub** 平台公布结果。  

如有疑问，请随时与我们联系。


## 致谢


我们衷心感谢所有对本项目给予支持和帮助的单位与个人。🎉🎉🎉  

同时，向参与本项目的全体成员表示诚挚的感谢！ 



