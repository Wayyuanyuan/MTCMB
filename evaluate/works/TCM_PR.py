import ast

def get_list(raw):
    if isinstance(raw, list):# 已是列表
        return [str(item).strip() for item in raw]
    if not isinstance(raw, str):
        return []

    raw = raw.strip()

    # 尝试用 ast.literal_eval 直接解析
    try:
        result = ast.literal_eval(raw)
        if isinstance(result, list):
            return [str(item).strip() for item in result]
    except:
        pass

    # 否则尝试提取中文/中文+数字/词组，给它加上引号再用 eval
    content = raw.strip("[]")
    parts = [s.strip() for s in content.split(",") if s.strip()]
    fixed = "[" + ", ".join(f'"{p}"' for p in parts) + "]"

    try:
        return ast.literal_eval(fixed)
    except:
        return []


def tcm_pr(standard_data: dict, llm_data: dict):
    gold = set(get_list(standard_data["answer"]))
    pred = set(get_list(llm_data["answer"]))

    intersection = gold & pred
    union = gold | pred

    jaccard = len(intersection) / len(union) if union else 0
    recall = len(intersection) / len(gold) if gold else 0
    precision = len(intersection) / len(pred) if pred else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    avg_herb = 1 - abs(len(gold) - len(pred)) / max(len(gold), len(pred))

    task2_score = (jaccard + f1 + avg_herb) / 3

    return {
        "Jaccard": jaccard,
        "Recall": recall,
        "Precision": precision,
        "F1_Score": f1,
        "Avg_Herb_Num_Match": avg_herb,
        "Task2_Score": task2_score
    }
