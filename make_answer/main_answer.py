import json
import os
from concurrent.futures import ThreadPoolExecutor

import tqdm
from loguru import logger

from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.works import question_prompt_dict


def chat_process(
    chat_invoker: ChatInvoker,prompt_type:int, model_name: str,
    data_root: str, output_root: str = "output", num_process: int = 1
):
    """答案生成主流程

        Args:
            prompt_type:设置使用zero-shot、few-shot还是带CoT的提示词
            chat_invoker: 聊天模型调用器实例（需实现具体问答逻辑）
            model_name: 模型名称（用于输出路径标识）
            data_root: 输入数据根目录（包含多个JSONL文件）
            output_root: 输出根目录（默认"output"） ，传递过来的是output/模型名
            num_process: 并发线程数（实际使用线程池控制并发）
        """
    # 创建线程池
    with ThreadPoolExecutor(max_workers=num_process) as executor:
        # 遍历输入目录中的所有数据文件
        for data_file in os.listdir(data_root):
            data_path = os.path.join(data_root, data_file) # 构建完整文件路径
            logger.info(f"Start process {data_path}")

            # 构建输出目录（格式：output_root/数据集名_不含后缀jsonl）
            output_dir = os.path.join(output_root,os.path.splitext(data_file)[0])
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)   # 创建多级目录

            # 中间文件路径（用于断点续传）
            mid_file = os.path.join(output_dir, "mid.jsonl")
            line_count = 0

            # 断点续传机制：如果中间文件存在，跳过已处理行
            if os.path.exists(mid_file):
                print(mid_file)
                # 统计已有行数（使用生成器表达式节省内存）
                with open(mid_file, encoding="utf-8") as f:
                    line_count = sum(1 for _ in f)
                if line_count:
                    logger.info(f"Find {line_count} lines, skip")

            # 读取需要处理的数据行
            data_lines = []
            total_count = 0
            with open(data_path, encoding="utf-8") as f:
                for i, line in enumerate(f):
                    total_count += 1
                    if i < line_count:  # 跳过已处理的行
                        continue
                    data_lines.append(json.loads(line))

            # 初始化进度条（动态描述显示文件名和模型名）
            process_bar = tqdm.tqdm(total=total_count, desc=f"{data_file} use {model_name} Process", unit="line")

            if line_count:
                process_bar.update(line_count)  # 更新已处理进度

            # 动态选择处理函数（根据文件名前缀匹配question_prompt_dict）
            if data_file[0].isalpha():
                work_func = question_prompt_dict[data_file[0]]   # 按首字母匹配
            else:
                work_func = question_prompt_dict[data_file.split(".")[0]]  # 按文件名前缀匹配

            # 批量处理数据
            if data_lines:
                # 使用线程池映射处理（每个data_line对应一个任务）
                # [chat_invoker]*N 创建参数列表，为每个任务传递相同chat_invoker实例
                for data in executor.map(
                    work_func, [prompt_type] * len(data_lines), data_lines, [chat_invoker] * len(data_lines)  # 生成等长参数列表
                ):
                    process_bar.update()

                    # 追加写入结果（确保UTF-8编码，禁用ASCII转义）
                    with open(mid_file, "a", encoding="utf-8") as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                        f.write("\n")

            process_bar.close()

