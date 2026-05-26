import json
import os
from concurrent.futures import ThreadPoolExecutor

import tqdm
from loguru import logger

from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.works import question_prompt_dict
from mtcmb_datasets import (
    CANONICAL_DATA_ROOT,
    Purpose,
    _should_include,
    iter_benchmark_files,
    load_records,
    shot_from_prompt_type,
)


def _load_processed_ids(mid_file: str) -> set[int]:
    """断点续传：按已写入 mid.jsonl 的 id 跳过，避免 few-shot 下行号与题号错位。"""
    done: set[int] = set()
    if not os.path.exists(mid_file):
        return done
    with open(mid_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec.get("id") is not None:
                done.add(int(rec["id"]))
    return done


def _apply_record_filters(
    data_lines: list[dict],
    *,
    limit: int | None = None,
    ids: set[int] | None = None,
) -> list[dict]:
    if ids:
        data_lines = [r for r in data_lines if int(r.get("id", -1)) in ids]
    if limit is not None and limit > 0:
        data_lines = data_lines[:limit]
    return data_lines


def chat_process(
    chat_invoker: ChatInvoker,prompt_type:int, model_name: str,
    data_root: str, output_root: str = "output", num_process: int = 1,
    datasets: list[str] | None = None,
    limit: int | None = None,
    ids: set[int] | None = None,
):
    """答案生成主流程

        Args:
            prompt_type:设置使用zero-shot、few-shot还是带CoT的提示词
            chat_invoker: 聊天模型调用器实例（需实现具体问答逻辑）
            model_name: 模型名称（用于输出路径标识）
            data_root: 输入数据根目录（包含多个JSONL文件）
            output_root: 输出根目录（默认"output"） ，传递过来的是output/模型名
            num_process: 并发线程数（实际使用线程池控制并发）
            datasets: 仅处理这些数据集文件名（如 3.TCM_FT_question_points.jsonl）
            limit: 最多再处理多少条（试跑可设 1；0/None 表示不限制）
            ids: 仅处理指定 id（如 {1}）
        """
    dataset_filter = (
        {f.strip() for f in datasets if f.strip()} if datasets else None
    )
    # 创建线程池
    with ThreadPoolExecutor(max_workers=num_process) as executor:
        shot = shot_from_prompt_type(prompt_type)
        use_loader = os.path.normpath(data_root) == os.path.normpath(str(CANONICAL_DATA_ROOT))

        file_iter = (
            iter_benchmark_files()
            if use_loader
            else ((f, os.path.join(data_root, f)) for f in os.listdir(data_root))
        )

        for data_file, data_path in file_iter:
            if not data_file.endswith(".jsonl") or data_file.startswith("._"):
                continue
            if dataset_filter and data_file not in dataset_filter:
                continue
            logger.info(f"Start process {data_path} (shot={shot.value})")

            # 构建输出目录（格式：output_root/数据集名_不含后缀jsonl）
            output_dir = os.path.join(output_root,os.path.splitext(data_file)[0])
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)   # 创建多级目录

            mid_file = os.path.join(output_dir, "mid.jsonl")
            processed_ids = _load_processed_ids(mid_file)
            if processed_ids:
                logger.info(
                    f"Resume {mid_file}: skip {len(processed_ids)} id(s), "
                    f"e.g. {sorted(processed_ids)[:8]}"
                )

            if use_loader:
                all_lines = load_records(
                    data_file, purpose=Purpose.BENCHMARK, shot=shot,
                )
                data_lines = [
                    r for r in all_lines
                    if int(r["id"]) not in processed_ids
                ]
                data_lines = _apply_record_filters(
                    data_lines, limit=limit, ids=ids,
                )
                total_count = len(all_lines)
                done_count = total_count - len(data_lines)
            else:
                data_lines = []
                with open(data_path, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        rec = json.loads(line)
                        rid = rec.get("id")
                        if rid is None:
                            continue
                        rid = int(rid)
                        if not _should_include(data_file, rid, shot):
                            continue
                        if rid in processed_ids:
                            continue
                        data_lines.append(rec)
                data_lines = _apply_record_filters(
                    data_lines, limit=limit, ids=ids,
                )
                total_count = len(data_lines) + len(processed_ids)
                done_count = len(processed_ids)

            if data_lines:
                logger.info(
                    f"Next id(s): {[int(r['id']) for r in data_lines[:5]]}"
                    f"{'...' if len(data_lines) > 5 else ''} (shot={shot.value})"
                )

            process_bar = tqdm.tqdm(
                total=total_count, desc=f"{data_file} use {model_name} Process", unit="line",
            )
            if done_count:
                process_bar.update(done_count)

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

