**数据集描述**：该数据集题目从中医中级主治医师考试的 12 个学科中随机抽取，共 1200 道题，用于评估大语言模型的中医基础知识。

**数据集来源**：中医中级主治医师考试的 12 个学科，具体包括推拿（按摩）学、中医儿科学、中医耳鼻喉科学、中医妇科学、中医肛肠科学、中医骨伤科学、中医内科学、中医皮肤与性病学、中医全科学、中医外科学、中医眼科学、中医针灸学

**元数据**

```
question：题干
options：选项
answer：答案
```

**评估指标**：Accuracy

**数据示例**

```
[
    "id": 1,
        "question": "患儿男性，4岁，因“发热4天，高热持续，头痛剧烈，呕吐频繁，颈背强直，烦躁谵语，四肢抽搐”来诊。患儿喉中痰鸣，唇干渴饮，溲赤便结，舌质红绛，苔黄厚，脉数有力，指纹紫滞。治疗应首选的方剂是",
        "options": {
            "A": "犀角地黄汤",
            "B": "清瘟败毒饮",
            "C": "羚角钩藤汤",
            "D": "安宫牛黄丸",
            "E": "镇肝熄风汤"
        },
        "answer": "B"
    }
]
 
        
```

