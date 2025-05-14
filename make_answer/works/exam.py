import re

from make_answer.chat.chat_invoker import ChatInvoker


def exam(data: dict, llm: ChatInvoker) -> dict:
    prompt = f'''以下是一道考题，有A、B、C、D、E五个备选答案，请从中选择一个最佳答案。
                #注意：输出只能在A、B、C、D、E五个答案选项中，选择一个最佳答案，不需要解释，禁止返回其他内容。
                题目：{data["question"]}。选项：{str(data["options"])}'''

    response = llm.chat(prompt)
    # 直接匹配 A、B、C、D、E 五个选项（不区分大小写）
    extract_choice = re.compile(r".*?([A-Ea-e]).*", re.DOTALL)

    # 从 response 中提取第一个匹配的选项字母（转为大写）
    match = extract_choice.match(response)
    data["answer"] = match.group(1).upper() if match else ""

    return data