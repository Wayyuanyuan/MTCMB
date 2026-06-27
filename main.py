import argparse
import importlib
import os
import os.path

from mtcmb_env import load_dotenv

load_dotenv()

from make_answer.chat import name_model_dict
from make_answer.chat.api_llm_workers import LlmApiWorkers
from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.chat.local_llm_workers import LlmLocalWorkers
from make_answer.main_answer import chat_process

_MODEL_TYPE_ENV: dict[str, str] = {
    "taiyi": "LOCAL_MODEL_TAIYI",
    "wingpt2": "LOCAL_MODEL_WINGPT2",
    "huatuo2": "LOCAL_MODEL_HUATUO",
    "baichuan": "LOCAL_MODEL_BAICHUAN",
    "disc_medllm": "LOCAL_MODEL_DISC_MEDLLM",
}


def _resolve_local_model_path(local_model: str | None, model_type: str | None) -> str | None:
    if local_model:
        raw = local_model.strip()
        if not raw:
            pass
        elif raw in os.environ and os.path.isdir(os.environ[raw].strip()):
            return os.environ[raw].strip()
        elif os.path.isdir(raw):
            return raw
        else:
            raise ValueError(
                f"无效的 --local-model: {raw!r}（路径不存在，且不是 .env 中的变量名）"
            )
    if model_type:
        env_key = _MODEL_TYPE_ENV.get(model_type)
        if env_key:
            path = os.environ.get(env_key, "").strip()
            if path and os.path.isdir(path):
                return path
    return None


def _output_root(prompt_type: int, model_name: str) -> str:
    if prompt_type == 1:
        return os.path.join("output_few_shot", model_name)
    if prompt_type == 2:
        return os.path.join("output_CoT", model_name)
    return os.path.join("output", model_name)


def parse_args():
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='TCM Assessment Benchmarks by \u7d2b\u613f\u5c3d\u597d')
    # 使用argparse解析命令行参数，获取输入文件路径、模型名称、进程数量
    # 添加所有命令行参数
    parser.add_argument(
        "--step-chat",
        type=str,
        default=None,
        help="模型做题数据目录（如 data/）；仅 --step-evaluate 时不要传此参数",
    )

    parser.add_argument('--prompt-type', type=int, default=0, help='设置提示词类型，0代表zero-shot,1代表few-shot,2代表CoT')

    parser.add_argument('--local-model', type=str, help='本地模型的绝对路径')
    parser.add_argument("--model-type", type=str,help=f"模型类型必须为以下之一：{list(name_model_dict.keys())}")

    parser.add_argument('--num-gpus', type=str, default="0", help='使用的GPU数量')

    parser.add_argument("--api-model", type=str,help="API模型类名，格式：模块.类名（必须继承自ChatInvoker）")
    parser.add_argument("--llm-name", type=str, help="API模型名称")
    parser.add_argument("--base-url", type=str, help="API基础URL")
    parser.add_argument("--api-key", type=str, help="API密钥")
    parser.add_argument(
        "--openrouter-model",
        type=str,
        default="",
        help="OpenRouter 模型 slug（如 deepseek/deepseek-chat），覆盖 .env 中 OPENROUTER_MODEL",
    )
    parser.add_argument(
        "--datasets",
        type=str,
        default="",
        help="仅生成指定数据集（逗号分隔文件名），如 TCM-FT.jsonl",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="最多再处理 N 条（试跑可设 1；0 表示全部）",
    )
    parser.add_argument(
        "--ids",
        type=str,
        default="",
        help="仅处理指定 id，逗号分隔，如 1 或 1,5,10",
    )

    parser.add_argument("--step-evaluate", type=str,help="运行答案评估步骤，必须设置答案文件路径")

    parser.add_argument(
        "--standard-answer-root",
        type=str,
        default="data",
        help="标准答案根目录（推荐与 --step-chat 同为 data/，评测时按 prompt-type 加载）",
    )
    parser.add_argument('--num-process', type=int, default=1, help='使用的进程数量')
    parser.add_argument("--sleep-time", type=float, default=0, help="请求间隔时间（秒）")

    # parser.add_argument("--step-chat", type=str, help="run get answer from LLM")
    #
    # parser.add_argument('--local-model', type=str, help='Local model absolute path')
    # parser.add_argument("--model-type", type=str, help=f"Model type must in {list(name_model_dict.keys())}")
    #
    # parser.add_argument('--num-gpus', type=str, default="0", help='Number of GPUs to use')
    #
    # parser.add_argument("--api-model", type=str, help="API model, need input model class name. The module in which the API model class resides, Must be inherited from ChatInvoker. Example module.class")
    # parser.add_argument("--llm-name", type=str, help="API model name")
    # parser.add_argument("--base-url", type=str, help="API base url")
    # parser.add_argument("--api-key", type=str, help="API key")
    #
    # parser.add_argument("--step-evaluate", type=str, help="run get score from answer, must set answer file path")
    #
    # parser.add_argument("--standard-answer-root", type=str, help="standard answer root")
    # parser.add_argument('--num-process', type=int, default=1, help='Number of GPUs to use')
    # parser.add_argument("--sleep-time", type=float, default=0, help="sleep time")

    return parser.parse_args()


def step_chat(_args: argparse.Namespace, *args, **kwargs):
    if not os.path.isdir(_args.step_chat):
        raise ValueError(f"Invalid chat file path: {_args.step_chat}, must be a directory")

    local_model_path = _resolve_local_model_path(_args.local_model, _args.model_type)

    if local_model_path:
        model_type = _args.model_type
        if not model_type:
            raise ValueError("使用本地模型时必须指定 --model-type（如 baichuan / taiyi）")
        if model_type not in name_model_dict:
            raise ValueError(
                f"Invalid model type: {model_type}, must be one of {list(name_model_dict.keys())}"
            )
        model_cls = name_model_dict[model_type]
        workers = LlmLocalWorkers()
        workers.init(
            local_model_path, model_cls, _args.num_process, _args.num_gpus, _args.sleep_time,
        )
        model_name = _args.llm_name or os.path.basename(local_model_path.rstrip("/"))
    elif _args.api_model:
        if _args.openrouter_model and _args.openrouter_model.strip():
            os.environ["OPENROUTER_MODEL"] = _args.openrouter_model.strip()
        workers = LlmApiWorkers()
        module_name, cls_name = _args.api_model.rsplit(".", 1)
        module = importlib.import_module(module_name)
        cls = getattr(module, cls_name)
        if not issubclass(cls, ChatInvoker):
            raise TypeError(f"{_args.api_model} must inherit from ChatInvoker")
        if not _args.llm_name:
            raise ValueError("使用 API 模型时必须指定 --llm-name")
        model_name = _args.llm_name
        workers.init(
            cls, _args.num_process,
            *args, model_name=model_name,
            base_url=_args.base_url, api_key=_args.api_key, sleep_time=_args.sleep_time, **kwargs,
        )
    else:
        raise ValueError(
            "请指定 --model-type（路径在 .env），或 --local-model + --model-type，"
            "或 --api-model + --llm-name"
        )

    output_path = _output_root(_args.prompt_type, model_name)
    # 启动聊天处理流程
    dataset_list = [s.strip() for s in _args.datasets.split(",") if s.strip()] or None
    record_limit = _args.limit if _args.limit and _args.limit > 0 else None
    id_set = (
        {int(x.strip()) for x in _args.ids.split(",") if x.strip()}
        if _args.ids.strip()
        else None
    )
    chat_process(
        workers, _args.prompt_type, model_name, _args.step_chat,
        output_root=output_path, num_process=_args.num_process,
        datasets=dataset_list,
        limit=record_limit,
        ids=id_set,
    )


def step_evaluate(_args: argparse.Namespace):
    from evaluate.main_evaluate import evaluate_process  # 动态导入评估模块

    chat_answers_root = _args.step_evaluate

    if not os.path.isdir(chat_answers_root):
        raise ValueError(f"Invalid answers root: {chat_answers_root}, must be a directory")

    evaluate_process(
        _args.standard_answer_root,
        chat_answers_root,
        output_path=chat_answers_root,
        num_process=_args.num_process,
        prompt_type=_args.prompt_type,
    )


if __name__ == '__main__':
    args = parse_args()

    if not args.step_chat and not args.step_evaluate:
        raise ValueError("请指定 --step-chat（生成答案）或 --step-evaluate（打分）")

    if args.step_chat:
        step_chat(args)

    if args.step_evaluate:
        step_evaluate(args)
