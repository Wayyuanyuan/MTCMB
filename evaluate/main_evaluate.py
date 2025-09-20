import glob
import json
import os.path
from concurrent.futures.thread import ThreadPoolExecutor

import pandas as pd
import tqdm

from loguru import logger

from evaluate.works import question_standard_dict


def evaluate_process(
    standard_answer_root: str, chat_answer_root: str, *args, **kwargs
):
    """
       评估处理主函数：比较模型生成的答案与标准答案

       Args:
           standard_answer_root: 标准答案根目录路径
           chat_answer_root: 待评估答案根目录路径
           *args, **kwargs: 可变参数，其中kwargs可能包含num_process（并发进程数）
       """
    all_summary = []  # 收集所有结果，最终写入 summary_score.xlsx

    # 遍历所有待评估的答案文件（递归查找mid.jsonl文件）
    for chat_answer_file in glob.glob(chat_answer_root + "/**/mid.jsonl", recursive=True):
        # 跳过非文件或非jsonl文件
        if not os.path.isfile(chat_answer_file) or os.path.splitext(chat_answer_file)[1] != ".jsonl":
            continue

        # 获取答案类别（即mid.jsonl文件所在目录名）也就是数据集名称,例如1.TCM_ED_A
        chat_answer_kind = os.path.basename(os.path.dirname(chat_answer_file))
        output_dir = os.path.dirname(chat_answer_file)
        output_file = os.path.join(output_dir, "score.json")  # 评分结果文件路径

        # 构建对应的标准答案文件路径
        standard_answer_file = os.path.join(standard_answer_root, chat_answer_kind + '.jsonl')
        if not os.path.isfile(standard_answer_file):
            logger.error(f"Can not find standard answer file {standard_answer_file}")
            continue

        logger.info(f"File({chat_answer_file}) use standard answer file({standard_answer_file})")

        # 根据问题类别选择评估函数
        if chat_answer_kind[0].isalpha():
            work_func = question_standard_dict[chat_answer_kind[0]]  # 按首字母匹配
        else:
            work_func = question_standard_dict[chat_answer_kind.split(".")[0]]  # 按前缀匹配

        # 如果没有score.json，先进行评分计算
        if not os.path.exists(output_file):
            # 读取待评估答案和标准答案
            with open(chat_answer_file, encoding="utf8") as f:
                chat_answer_data = [json.loads(line) for line in f]
                # for i, line in enumerate(f):
                #     try:
                #         chat_answer_data = json.loads(line)
                #     except json.JSONDecodeError as e:
                #         print(f"JSON decode error on line {i + 1}: {e}")
                #         print(f"Problematic line: {line}")
                #         break
            with open(standard_answer_file, encoding="utf8") as f:
                standard_answer_data = [json.loads(line) for line in f]

            # 检查数据量是否匹配
            if len(chat_answer_data) != len(standard_answer_data):
                logger.error(
                    f"Data size not match, chat_answer({len(chat_answer_data)}) standard_answer({len(standard_answer_data)})")
                continue

            num_process = kwargs.get("num_process", 1)  # 获取并发进程数，默认为1

            scores = []    # 存储评分结果
            # 初始化进度条
            process_bar = tqdm.tqdm(total=len(chat_answer_data), desc=f"{chat_answer_kind} Evaluate", unit="line")

            # 使用线程池并发评估
            with ThreadPoolExecutor(max_workers=num_process) as executor:
                for result in executor.map(work_func, standard_answer_data, chat_answer_data):
                    scores.append(result)
                    process_bar.update(1)

            # 保存评分结果
            with open(output_file, "w", encoding="utf8") as f:
                output_data = json.dumps(scores, ensure_ascii=False, indent=4)
                f.write(output_data)
            logger.info(f"Save score to {output_file}")
        else:
            logger.info(f"Already evaluated {chat_answer_kind}, load existing score")

        # 加载评分文件
        with open(output_file, encoding="utf8") as f:
            scores = json.load(f)

        # 计算综合得分（根据不同问题类型采用不同计算方式）
        if chat_answer_kind in ["1.TCM_ED_A", "2.TCM_ED_B", "7.TCM_MSDD",  "12.TCM_DC_B"]:
            score = sum(scores) / len(scores) * 100
        elif chat_answer_kind in ["11.TCM_DC_A"]:
            scores_float = [float(x) for x in scores]
            score = sum(scores_float) / len(scores) * 100
        elif chat_answer_kind in ["9.TCM_PR"]:
            score = sum([s["Task2_Score"] for s in scores if isinstance(s, dict)]) * 100 // len(scores)
        elif chat_answer_kind in ["3.TCM_FT"]:
            score = sum([s["bert"] for s in scores if isinstance(s, dict)]) * 100 // len(scores)
        elif chat_answer_kind in["6.TCM_LitData"]:
            score = sum([((s["rouge_1"] * 100 + s["rouge_l"] * 100) / 2 + s["bleu"]) / 2
                         for s in scores if isinstance(s, dict)]) // len(scores)
        elif chat_answer_kind in ["4.TCMeEE", "5.TCM_CHGD", "8.TCM_DiagData", "10.TCM_FRD"]:
            score = sum([((s["rouge_1"]*100 + s["rouge_l"]*100) / 2 + s["bert"] *100+ s["bleu"]) / 3
                         for s in scores if isinstance(s, dict)])// len(scores)
        else:
            score = "/"

        # 添加到汇总列表中
        all_summary.append({"question_name": chat_answer_kind, "score": score})

    # 最后统一生成 summary_score.xlsx
    summary_path = os.path.join(chat_answer_root, "summary_score.xlsx")
    summary_score_df = pd.DataFrame(all_summary)

    if os.path.exists(summary_path):
        exists_df = pd.read_excel(summary_path)
        if "question_name" not in exists_df.columns or "question_name" not in summary_score_df.columns:
            raise ValueError(f"Key column 'question_name' does not exist in one of the DataFrames.")

        merged_df = pd.merge(exists_df, summary_score_df, on="question_name", how='outer', suffixes=('', '_new'))
        for col in summary_score_df.columns:
            if col != "question_name":
                merged_df[col] = merged_df[col + '_new'].combine_first(merged_df[col])
                if col + '_new' in merged_df.columns:
                    merged_df.drop(columns=[col + '_new'], inplace=True)
        merged_df.to_excel(summary_path, index=False)
    else:
        summary_score_df.to_excel(summary_path, index=False)

    logger.info(f"Summary score written to {summary_path}")