# MTCMB 多任务中医评估基准 

<center>

![Python 3.12](https://img.shields.io/badge/Python-3.12-lightblue) ![Torch 2.3.1](https://img.shields.io/badge/PyTorch-2.3.1-lightblue) ![OpenAi 1.25.0](https://img.shields.io/badge/openai-1.25.0-lightblue) ![bert-score](https://img.shields.io/badge/bert--score-0.3.13-lightblue)
</center>


<p align="center">
   📃 <a href="https://doi.org/10.5281/zenodo.20465629" target="_blank">Zenodo</a> • 🌐 <a href="https://github.com/Wayyuanyuan/MTCMB" target="_blank">GitHub</a>  
   <br>  <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe_cn.md">   中文</a> | <a href="https://github.com/Wayyuanyuan/MTCMB/blob/main/ReadMe.md"> English
</p>


## 🌈 更新

- **[2025.5.15]** 发布了论文。
- **[2025.5.15]** 🎉🎉🎉 MTCMB 正式发布！🎉🎉🎉

## 🌐 数据下载

共 **12** 个子数据集、**7,100** 条样本，以 JSONL 格式存放于 `data/` 目录。

（1）从 [GitHub](https://github.com/Wayyuanyuan/MTCMB) 获取完整项目（数据、评估代码与文档）

```bash
git clone https://github.com/Wayyuanyuan/MTCMB.git
cd MTCMB/data
```

克隆后数据位于 `data/*.jsonl`（每条含 `answer` 与 `source`）。

（2）从 [Zenodo](https://doi.org/10.5281/zenodo.20465629) 下载数据集归档（CC-BY 4.0）

Zenodo 提供 **12** 个子集 JSONL 文件；下载后置于本地 `data/` 目录即可。

## 📍排行榜​​
#### 🔆通用大模型

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.TCM-SE-A | 12.TCM-SE-B |
| -------------------- | ---------- | ---------- | --------- | -------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | ------- |
| gpt-4.1 | 64.67 | 75.15 | 71.81 | 52 | 55 | 64 | 35 | 49 | 35 | 49 | 70.99 | 74 |
| gpt-4.1 Few-Shot | 72.01 | 74.25 | 71.78 | 78 | 48 | 59 | 34.44 | 51 | 40 | 54 | 73.15 | 72.34 |
| gpt-4.1 CoT | 73.02 | 72.05 | 72.05 | 72 | 47 | 64 | 35.46 | 51 | 40 | 54 | 72.76 | 68.09 |
| claude | 59.42 | 59.58 | 71.09 | 69 | 50 | 56 | 12.75 | 39 | 31 | 36 | 58.76 | 48 |
| claude Few-Shot | 64.24 | 62.96 | 72.1 | 79 | 51 | 55 | 38.52 | 44 | 38 | 38 | 64.94 | 55.32 |
| claude CoT | 63.99 | 51.68 | 72.27 | 54 | 43 | 57 | 30.87 | 41 | 34 | 39 | 48.83 | 53.19 |
| gemini | 83.5 | 86.6 | 71.21 | 77 | 46 | 65 | 32.25 | 46 | 37 | 39 | 82.04 | 86 |
| gemini Few-Shot | 85.05 | 87.22 | 73.17 | 75 | 48 | 57 | 35.71 | 47 | 40 | 50 | 82.37 | 87.23 |
| gemini CoT | 85.71 | 66.69 | 72.6 | 79 | 47 | 62 | 34.95 | 47 | 38 | 50 | 77.8 | 85.11 |
| qwen-max | 86.92 | 90.54 | 72.15 | 51 | 50 | 68 | 30 | 49 | 36 | 44 | 77.16 | 78 |
| qwen-max Few-Shot | 88.14 | 90.43 | 73.02 | 80 | 50 | 65 | 40.05 | 52 | 40 | 54 | 79.11 | 82.98 |
| qwen-max CoT | 86.72 | 75.42 | 72.88 | 51 | 49 | **71** | 38.01 | **53** | 40 | 54 | 77.83 | 80.85 |
| glm-4-plus | 83.83 | 87.25 | 73.03 | 82 | 47 | 64 | 32.5 | 46 | 37 | 38 | 72.73 | 74 |
| glm-4-plus Few-Shot | 82.54 | 86.64 | 73.68 | 80 | 49 | 62 | 40.05 | 47 | 40 | 51 | 78.26 | 74.47 |
| glm-4-plus CoT | 82.04 | 80.53 | 72.35 | 82 | 48 | 63 | 37.24 | 34 | **41** | 50 | 78.96 | 74.47 |
| doubao | **92.08** | **94.21** | 73.77 | 86 | 46 | 67 | 33.75 | 50 | 37 | 52 | 83.16 | **90** |
| doubao Few-Shot | 91.48 | 94.04 | 73.91 | 83 | **56** | 62 | 39.54 | 51 | 39 | **58** | 83.18 | 87.23 |
| doubao CoT | 91.73 | 83.97 | 75.04 | 86 | 50 | 34 | 37.5 | 51 | 39 | 54 | 81.17 | 85.11 |
| DeepSeek-V3 | 89.08 | 91.17 | 71.92 | **87** | 48 | 62 | 39.25 | 50 | 39 | 41 | **85.86** | 82 |
| DeepSeek-V3 Few-Shot | 89.64 | 90.95 | 73.1 | 83 | 52 | 61 | **41.33** | 51 | 40 | 56 | 85.25 | 80.85 |
| DeepSeek-V3 CoT | 88.47 | 80.11 | 73.3 | 86 | 51 | 62 | 38.78 | 51 | 40 | 54 | 81.02 | 74.47 |





#### 🔆推理大模型

#### 

| Model                | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.TCM-SE-A | 12.TCM-SE-B |
| -------------------- | ---------- | ---------- | --------- | -------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | --------- |
| o4-mini | 70.92 | 74.42 | 68.82 | 78 | 45 | 61 | 17.25 | 51 | 26 | 43 | 55.3 | 54 |
| o4-mini Few-Shot | 69.92 | 74.34 | 69.32 | 79 | 47 | **64** | 28.06 | **52** | 38 | 52 | 58.55 | 70.21 |
| qwen3-235B | 86.83 | 91.54 | 71.16 | 53 | **58** | 60 | 42 | 49 | 35 | 46 | 71.36 | 86 |
| qwen3-235B Few-Shot | 87.13 | 89.58 | 72.58 | 79 | 50 | 60 | **50** | 50 | 40 | **54** | 70.32 | 80.85 |
| DeepSeek-r1 | 89.08 | 91.17 | 73.08 | **87** | 48 | 62 | 39.25 | 50 | 39 | 41 | **85.86** | 82 |
| DeepSeek-r1 Few-Shot | **92.40** | **92.33** | 73.82 | 83 | 52 | 61 | 40.05 | 49 | **41** | 52 | 86.26 | **89.36** |




#### 🔆医学专业大模型

#### 

| Model            | 1.TCM-ED-A | 2.TCM-ED-B | 3.TCM-FT  | 4.TCMeEE | 5.TCM-CHGD | 6.TCM-LitData | 7.TCM-MSDD | 8.TCM-Diagnosis | 9.TCM-PR | 10.TCM-FRD | 11.TCM-SE-A | 12.TCM-SE-B |
| ---------------- | ---------- | ---------- | --------- | --------- | ---------- | ------------- | ---------- | --------------- | -------- | ---------- | --------- | ------- |
| WINGPT2-14B-Chat | 40.25 | 40.98 | 68.39 | 57 | 40 | 44 | 17 | 45 | 22 | 35 | 43.2 | 46 |
| WINGPT2-14B-Chat Few-Shot | 41 | 44.9 | 68.6 | 69 | 44 | 38 | 23 | 48 | 21 | **43** | 39.38 | 44 |
| WINGPT2-14B-Chat CoT | 42.08 | 41.88 | 67.99 | 52 | 42 | 36 | 16.75 | 47 | 19 | 30 | 43.1 | 32 |
| TaiYi-LLM | 39.92 | 47.71 | 66.87 | 49 | 29 | **61** | 13.5 | 49 | 11 | 30 | 24.07 | 28 |
| TaiYi-LLM Few-Shot | 39.67 | 42.94 | 54.8 | 55 | 25 | 43 | 35.5 | 48 | 19 | 29 | 28.13 | 40 |
| TaiYi-LLM CoT | 39.17 | 39.54 | 62.57 | 32 | 32 | 47 | 31.75 | 35 | 10 | 29 | 25.73 | 30 |
| DISC-MedLLM | 31.33 | 32.42 | 65.93 | 45 | 34 | 19 | 3 | 44 | 19 | 26 | 35 | 0 |
| DISC-MedLLM Few-Shot | 27.17 | 29.31 | 58.44 | 31 | 28 | 22 | 1.5 | 38 | 17 | 32 | 37.42 | 2 |
| DISC-MedLLM CoT | 26.58 | 31.42 | 66.61 | 24 | 23 | 24 | 4 | 37 | 7 | 25 | 42.52 | 0 |
| HuatuoGPT-o1-72b | 75.17 | **82.27** | 71.3 | 82 | 45 | 40 | 20.25 | 45 | 24 | **45** | 51.3 | 70 |
| HuatuoGPT-o1-72b Few-Shot | 73 | 81.13 | 72.26 | 80 | **48** | 44 | 34.25 | 41 | 32 | 34 | 52.2 | 68 |
| HuatuoGPT-o1-72b CoT | 72 | 79.13 | 70.97 | 82 | **48** | 43 | 30 | 42 | 26 | 35 | 58.65 | 70 |
| Baichuan-14b-M1 | 79.83 | 82.02 | 72.47 | 82 | 46 | **63** | 35.5 | 46 | 33 | 38 | 70.36 | 66 |
| Baichuan-14b-M1 Few-Shot | 28.5 | 80.88 | 73.42 | 80 | 42 | 57 | **46.75** | **51** | **38** | 32 | 73.36 | **72** |
| Baichuan-14b-M1 CoT | **85.08** | 55.81 | 71.9 | **84** | 44 | 34 | 36.5 | **51** | 37 | 20 | **76.09** | 68 |

## 😊数据集描述

#### 结构

数据集：**5**个维度，**12**个数据集

五个评估维度及 12 个子数据集的数据量分布如下图所示

![MTCMB dataset distribution](https://github.com/Wayyuanyuan/MTCMB/blob/main/pics/Figure_1.png)

🥸 **知识问答**维度包含三个数据集，分别是TCM-ED-A（1200）、TCM-ED-B（4800）、TCM-FT（100）



- **知识问答**：通过中级主治医师和执业医师考试题目以及标准问答题形式，考察大模型对中医基础理论、方剂学、针灸学、诊断学等核心知识的理解与应用能力。

- **语言理解**：通过医案中的实体抽取、从医患对话生成结构化医案以及基于文献内容回答问题等形式，评估大模型在中医文本理解和信息抽取方面的表现力与准确性。

- **诊断推理**：考察大模型根据患者临床信息（如症状、体征、舌脉等）进行辨证分析，并准确判断疾病名称与证型的能力。

- **处方推荐**：评估大模型根据病情描述和证型特征，推荐合适中药方剂的能力，涵盖对方剂组成、配伍规律及病症对应关系的理解。

- **安全评估**：通过填空题与选择题的形式，考察大模型识别中医实践中涉及的安全风险，如有毒中药剂量控制、孕妇禁用药及针灸禁忌等内容，确保其具备基本的临床安全性判断能力。

  

#### 详细信息

**点击超链接可以查看到不同数据集格式要求**⬅️⬅️

| 维度         | 数据集名称    | 数量  | 任务描述                                               | 数据来源                                                     | 构建方式                                      | 评估方法                           |
| ------------ | ------------- | ----- | ------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------- | ---------------------------------- |
| 知识问答 | [TCM-ED-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-A.md)      | 1,200 | 12 学科五选一选择题（A–E）                           | 国家中医中级主治医师考试官方题库                             | 12 临床学科各分层抽样 100 题；三名执业医师专家审核 | 准确率                             |
|          | [TCM-ED-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-ED-B.md)     | 4800  | 执业医师全真模拟选择题                               | 国家中医执业医师资格考试官方题库                             | 8 套完整模拟卷（每套 600 题）随机抽样           | 准确率                             |
|          | [TCM-FT](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FT.md)       | 100   | 开放式问答题                                             | 《中医学问答题库》（胡熙明主编）                             | 随机抽样后经 DeepSeek-R1 语义改写并提取要点（`points`）；专家交叉验证 | BERTScore（要点对齐）              |
| 语言理解 | [TCMeEE](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCMeEE.md)        | 100   | 根据医案识别并抽取与中医相关的实体，生成结构化病历。   | [中医智库](https://zhongyigen.com/)（95%）及执业医师提交医案（5%） | DeepSeek-R1 自动生成结构化参考答案；专家复核 | BLEU、ROUGE、BERTScore 取平均      |
|          | [TCM-CHGD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-CHGD.md)      | 100   | 根据医患对话生成结构化病历。                           | 国家中医药管理局认证中心《中医执业助理/执业医师实践技能考试案例分析题库》 | 基于官方病案摘要，DeepSeek-R1 逆向生成模拟问诊对话；专家审核 | BLEU、ROUGE、BERTScore 取平均      |
|          | [TCM-LitData](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-LitData.md)   | 100   | 根据文献内容回答问题。                                 | [阿里云天池实验室的中医文献问题生成数据集](https://tianchi.aliyun.com/dataset/86895) | 从数据集随机抽取100道题目，并且由专业人员复核 | ROUGE 和 BLEU二者取平均            |
| 诊断推理 | [TCM-MSDD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-MSDD.md)      | 100   | 多标签证型（10 类）与疾病（4 类）分类。                | [CCL25-Eval 任务 9 子任务 1](https://tianchi.aliyun.com/competition/entrance/532301) | 保留原始标注并经专家复核                         | 准确率（多标签）                   |
|          | [TCM-Diagnosis](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-Diagnosis.md) | 200   | 根据症状表现给出疾病名称、证名、病位、病性。           | 国家“十三五”规划教材（中医内/外/妇/儿科学，各 50 例）        | 术语规范化临床表现作输入；执业医师标注结构化参考答案 | BLEU、ROUGE、BERTScore 取平均      |
| 处方推荐 | [TCM-PR](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-PR.md)        | 100   | 根据临床信息推荐中药方剂（药物集合匹配）。             | [CCL25-Eval 任务 9 子任务 2](https://tianchi.aliyun.com/competition/entrance/532301) | 保留原始标注；临床专家修订病案与参考答案 | Jaccard、Precision、Recall、F1、Size Agreement 及综合分 |
|          | [TCM-FRD](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-FRD.md)       | 200   | 根据证候表现给出治法、方剂名与药物组成。               | 国家“十三五”规划教材（与 TCM-Diagnosis 并行构建）            | 术语规范化临床表现作输入；执业医师标注           | BLEU、ROUGE、BERTScore 取平均      |
| 安全评估 | [TCM-SE-A](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SE-A.md) | 50    | 填空题（毒性、配伍禁忌、妊娠禁忌等）                   | 《中华人民共和国药典》（2020 年版）                          | DeepSeek-R1 合成临床情境填空题；专家审核         | GLM-4-Air-250414 模型评分          |
|          | [TCM-SE-B](https://github.com/Wayyuanyuan/MTCMB/blob/main/dataset_info/TCM-SE-B.md) | 50    | 选择题（用药与针灸安全）                               | 《中华人民共和国药典》（2020 年版）                          | 基于同一安全记录由 DeepSeek-R1 生成选择题；专家审核 | 准确率                             |

#### 目录结构

与论文 Data Record 一致，仓库包含两个主目录：

| 目录 | 说明 |
| ---- | ---- |
| [`data/`](data/) | **12** 个子数据集 JSONL（`*.jsonl`），每条样本含标准答案 `answer` 与溯源字段 `source` |
| [`dataset_info/`](dataset_info/) | 各子集元数据（`.md`）：数据来源、预处理、评估指标等 |

**数据获取**：[Zenodo](https://doi.org/10.5281/zenodo.20465629)（CC-BY 4.0）归档 **12** 个子集数据文件；[GitHub](https://github.com/Wayyuanyuan/MTCMB) 提供完整项目（含 `data/`、评估脚本与文档）。Few-shot / zero-shot 通过 `mtcmb_datasets.load_records(..., shot=...)` 派生题集，无需单独 `data_few_shot/` 目录。详见 [`dataset_info/数据记录.md`](dataset_info/数据记录.md)。

## 🔆如何提交和评估

### 环境配置

确保你的开发环境已经安装了 [requirements.txt](https://github.com/Wayyuanyuan/MTCMB/blob/main/requirements.txt) 中的 Python 依赖。

#### 环境变量（`.env`）

仓库根目录提供模板文件 **[`.env.example`](.env.example)**。使用前复制为 `.env` 并填写密钥与本地模型路径：

```bash
cp .env.example .env
# 编辑 .env，至少配置一种调用方式（OpenAI 兼容 API 或 OpenRouter 或本地模型路径）
```

`main.py` 启动时会通过 `mtcmb_env.load_dotenv()` 加载 `.env`（**不会覆盖**已存在的系统环境变量）。常用变量说明：

| 变量 | 用途 |
| ---- | ---- |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` | OpenAI 兼容 API 调用 |
| `OPENROUTER_API_KEY` / `OPENROUTER_MODEL` | OpenRouter 远程模型 |
| `DEEPSEEK_API_KEY` / `DEEPSEEK_MODEL` | DeepSeek 脚本（如 TCM-FT enriched） |
| `LOCAL_MODEL_*` | 本地 HuggingFace 模型目录（配合 `--model-type`） |

#### 单元测试（zero-shot / few-shot / CoT）

无需真实 API 即可验证数据加载、三种 `prompt_type` 与评测管线：

```bash
python -m unittest discover -s tests -v
```

测试覆盖：`load_records` 的 zero/few 题集差异、CoT 与 zero-shot 共用题集、`TCM-ED-A`/`TCM-SE-B` 三种提示模板差异，以及基于标准答案的 `evaluate_process` 满分回归。

### 问答模块

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

### 评估模块

使用方式

```python
python main.py \
--step-evaluate LLM回答所在目录 \ # 一般情况下， 传入根目录下模型名称
--standard-answer-root 标准答案目录 # 传入标准答案目录
```



### 其他参数

 

| 参数名称      | 默认值 | 作用                               |
| ------------- | ------ | ---------------------------------- |
| --num-process | 1      | 调用大模型回答以及评估时并发线程数 |
| --sleep-time  | 0      | 大模型单次回答后，等待的时间。     |


## 

## 提交格式要求



我们的评估基准包括 **12** 个子数据集。零样本评测时，模型输入中 `answer` 字段留空（或由 `mtcmb_datasets.load_records` 自动清空）；标准答案保存在同一 `data/` 目录中供评测使用。一个简短的示例如下：

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
├── TCM-SE-A
│   └── mid.jsonl
└── TCM-SE-B
    └── mid.jsonl

```

请将文件以压缩包形式提交，例如 **gemini-1.5-pro.zip**。压缩包请发送至邮箱 **weiyy53@mail2.sysu.edu.cn**。
我们将在评估完成后，于 **GitHub** 平台公布结果。  

如有疑问，请随时与我们联系。


## 致谢


我们衷心感谢所有对本项目给予支持和帮助的单位与个人。🎉🎉🎉  

同时，向参与本项目的全体成员表示诚挚的感谢！ 



