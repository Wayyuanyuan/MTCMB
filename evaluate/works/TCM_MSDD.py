import json
from numpy import average

all_zheng = {'气虚血瘀':'气虚血瘀证', '痰瘀互结':'痰瘀互结证', '气阴两虚':'气阴两虚证', '气滞血瘀':'气滞血瘀证',
             '肝阳上亢':'肝阳上亢证', '阴虚阳亢':'阴虚阳亢证', '痰热蕴结':'痰热蕴结证', '痰湿痹阻':'痰湿痹阻证',
             '阳虚水停':'阳虚水停证', '肝肾阴虚':'肝肾阴虚证'}
all_disease = {'胸痹心痛':'胸痹心痛病', '心衰':'心衰病', '眩晕':'眩晕病', '心悸':'心悸病'}


def convert_fields_to_list(data, sep='|'):
    result = data.copy()
    if '证型' in result:
        result['证型'] = [item.strip() for item in result['证型'].split(sep)]
    if '疾病' in result:
        result['疾病'] = [item.strip() for item in result['疾病'].split(sep)]
    return result


#处理模型的回答为标准回答
def get_normal_answer(llm_data):
    ans_zheng_list =[]
    ans_disease_list = []

    for zheng in all_zheng:
        if zheng in llm_data:
            ans_zheng_list.append(all_zheng.get(zheng))

    for disease in all_disease:
        if disease in llm_data:
            ans_disease_list.append(all_disease.get(disease))

    normal_answer ={
        "证型":ans_zheng_list,
        "疾病":ans_disease_list
    }
    return normal_answer

def tcm_msdd(standard_data: dict, llm_data: dict):
    #标准答案统一处理为数组
    standard = convert_fields_to_list(standard_data["answer"])

    golden_zheng = standard["证型"]
    golden_disease = standard.get("疾病", [])  # 如果没有疾病字段，默认为空列表

    if not isinstance(golden_disease, list):
        golden_disease = [golden_disease]

    llm_data = llm_data["answer"]
    # # 如果以 ```json 或 ``` 开头，则去除
    # if llm_data.startswith("```json"):
    #     llm_data = llm_data[7:].lstrip()
    # elif llm_data.startswith("```"):
    #     text = llm_data[3:].lstrip()
    #
    # # 如果以 ``` 结尾，则去除
    # if llm_data.endswith("```"):
    #     llm_data = llm_data[:-3].rstrip()

    # # 分别提取模型回答的证型和疾病
    # try:
    #     if isinstance(llm_data, str):
    #         llm_data = json.loads(llm_data)
    #     ans_zheng = json.dumps(llm_data.get("证型"),ensure_ascii=False)
    #     ans_disease = llm_data.get("疾病")
    # except json.JSONDecodeError:
    #     print("error: 无法解析模型输出为JSON")
    #     return -1

    # 标准化处理
    normal_llm_ans = get_normal_answer(llm_data)

    # 证型得分计算
    zheng_score = 0
    zheng_sum = len(golden_zheng)

    for zheng in normal_llm_ans["证型"]:
        if zheng in golden_zheng:
            zheng_score+=1


    # 疾病得分计算
    disease_score = 0
    disease_sum = len(golden_disease)

    for disease in normal_llm_ans["疾病"]:
        if disease in golden_disease:
            disease_score+=1

    # 最终得分
    final_score = average([zheng_score / zheng_sum if zheng_sum > 0 else 0,
                           disease_score / disease_sum if disease_sum > 0 else 0])
    return  final_score
