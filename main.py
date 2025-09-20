import argparse
import importlib
import os.path

from make_answer.chat import name_model_dict
from make_answer.chat.api_llm_workers import LlmApiWorkers
from make_answer.chat.chat_invoker import ChatInvoker
from make_answer.chat.local_llm_workers import LlmLocalWorkers
from make_answer.main_answer import chat_process


def parse_args():
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='TCM Assessment Benchmarks by \u7d2b\u613f\u5c3d\u597d')
    # 使用argparse解析命令行参数，获取输入文件路径、模型名称、进程数量
    # 添加所有命令行参数
    parser.add_argument("--step-chat", type=str, help="运行从LLM获取答案的步骤，需要指定输入文件目录")

    parser.add_argument('--prompt-type', type=int, default=0, help='设置提示词类型，0代表zero-shot,1代表few-shot,2代表CoT')

    parser.add_argument('--local-model', type=str, help='本地模型的绝对路径')
    parser.add_argument("--model-type", type=str,help=f"模型类型必须为以下之一：{list(name_model_dict.keys())}")

    parser.add_argument('--num-gpus', type=str, default="0", help='使用的GPU数量')

    parser.add_argument("--api-model", type=str,help="API模型类名，格式：模块.类名（必须继承自ChatInvoker）")
    parser.add_argument("--llm-name", type=str, help="API模型名称")
    parser.add_argument("--base-url", type=str, help="API基础URL")
    parser.add_argument("--api-key", type=str, help="API密钥")

    parser.add_argument("--step-evaluate", type=str,help="运行答案评估步骤，必须设置答案文件路径")

    parser.add_argument("--standard-answer-root", type=str, help="标准答案根目录")
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
    # 检查输入目录有效性
    if not os.path.isdir(_args.step_chat):
        raise ValueError(f"Invalid chat file path: {_args.step_chat}, must be a directory")
    # 本地模型处理分支
    if _args.local_model:
        print("here")
        # 验证模型类型
        model_type = _args.model_type
        if model_type not in name_model_dict:
            raise ValueError(f"Invalid model type: {model_type}, must be one of {list(name_model_dict.keys())}")

        # 获取对应的模型类
        model_cls = name_model_dict[model_type]
        workers = LlmLocalWorkers()   # 创建本地工作器实例
        # 初始化工作器（模型路径、模型类、进程数、GPU数、间隔时间）
        workers.init(_args.local_model, model_cls, _args.num_process, _args.num_gpus, _args.sleep_time)

        # 从路径提取模型名称
        if _args.local_model.endswith("/"):
            model_name = os.path.basename(_args.local_model[:-1])
        else:
            model_name = os.path.basename(_args.local_model)
    # API模型处理分支
    else:
        workers = LlmApiWorkers() # 创建API工作器实例
        # 获取最后一个.号的字符
        module_name, cls_name = _args.api_model.rsplit(".", 1)
        module = importlib.import_module(module_name) # 动态导入模块
        cls = getattr(module, cls_name)    # 获取类对象

        # 验证是否继承自ChatInvoker
        if not issubclass(cls, ChatInvoker):
            raise TypeError(f"{_args.api_model} must inherit from ChatInvoker")

        model_name = _args.llm_name
        # 初始化API工作器（模型类、进程数、模型名称、API参数等）
        workers.init(
            cls, _args.num_process,
            *args, model_name=model_name,
            base_url=_args.base_url, api_key=_args.api_key, sleep_time=_args.sleep_time,**kwargs)

    # 设置输出路径（output/模型名称）
    if _args.prompt_type ==0:
        output_path = os.path.join("output",_args.llm_name)
    elif _args.prompt_type ==1:
        output_path = os.path.join("output_few_shot", _args.llm_name)
    else:
        output_path = os.path.join("output_CoT", _args.llm_name)
    # 启动聊天处理流程
    chat_process(workers, _args.prompt_type, model_name, _args.step_chat, output_root=output_path, num_process=_args.num_process)


def step_evaluate(_args: argparse.Namespace):
    from evaluate.main_evaluate import evaluate_process  # 动态导入评估模块

    chat_answers_root = _args.step_evaluate

    # 设置输出路径（output/模型名称）
    if _args.prompt_type == 0:
        output_path = os.path.join("output", _args.llm_name)
    elif _args.prompt_type == 1:
        output_path = os.path.join("output_few_shot", _args.llm_name)
    else:
        output_path = os.path.join("output_CoT", _args.llm_name)

    # 验证答案目录有效性
    if not os.path.isdir(chat_answers_root):
        raise ValueError(f"Invalid answers root: {chat_answers_root}, must be a directory")

    # 启动评估流程（标准答案目录、待评估答案目录、输出路径、进程数）
    evaluate_process(_args.standard_answer_root, chat_answers_root, output_path=output_path, num_process=_args.num_process)


if __name__ == '__main__':
    args = parse_args()

    if args.step_chat:
        step_chat(args)

    if args.step_evaluate:
        step_evaluate(args)
