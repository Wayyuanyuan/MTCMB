import re

from make_answer.chat.chat_invoker import ChatInvoker


def tcm_ed_b(prompt_type:int,data: dict, llm: ChatInvoker) -> dict:
    zero_shot_prompt = f'''以下是一道考题，有A、B、C、D、E五个备选答案，请从中选择一个最佳答案。
                #注意：输出只能在A、B、C、D、E五个答案选项中，选择一个最佳答案，不需要解释，禁止返回其他内容。
                题目：{data["question"]}。选项：{str(data["options"])}'''
    few_shot_prompt = f'''
        以下是一道考题，有A、B、C、D、E五个备选答案，请你选出最佳答案。
        注意：最终输出只能为A、B、C、D、E中的一个，不需要解释答案。
        ##请参考以下示例：
        #示例一:
        【题目】：足太阴脾经与手少阴心经的交接位置是  
        【选项】：A: 胸中  B: 肺中  C: 心中  D: 目内眦  E: 足大趾  
        【答案】C
        #示例二:
        【题目】：推动人体生长发育及脏腑功能活动的气是  
        【选项】：A: 卫气  B: 中气  C: 元气  D: 宗气  E: 营气  
        【答案】C
        #示例三：
        【题目】：津液的丢失往往伴有气的损耗，说明二者的关系是  
        【选项】：A: 气能行津  B: 气能摄津  C: 气能生津  D: 津能生气  E: 津能载气  
        【答案】：E
        #请你参考以上示例，回答下面问题，并从备选答案中选出最佳答案。注意：最终输出只能为A、B、C、D、E中的一个，只返回答案字母选项，禁止返回其他内容。题目：{data["question"]}。选项：{str(data["options"])}
    
'''
    cot_prompt = f'''
            以下是一道考题，有A、B、C、D、E五个备选答案，请你推理得出最佳答案。每题先推理，再输出答案。  
            注意：最终输出只能为A、B、C、D、E中的一个，不需要解释答案。
            ##请参考以下示例及其推理过程：
            #示例一:
            题目：足太阴脾经与手少阴心经的交接位置是  
            选项：A: 胸中  B: 肺中  C: 心中  D: 目内眦  E: 足大趾  
            推理过程：十二经脉中，足太阴脾经上达胸中，与手少阴心经在心中相交会。《灵枢·经脉》有载，脾经“上膈，挟咽，连舌本，散舌下”，并“上膈，注心中”。说明两经的交接处是在“心中”。  
            答案：C
            #示例二:
            题目：推动人体生长发育及脏腑功能活动的气是  
            选项：A: 卫气  B: 中气  C: 元气  D: 宗气  E: 营气  
            推理过程：元气是先天之精所化生，藏于肾，具有推动、生长、温煦等功能，是维持人体生命活动的基本动力。因此，推动生长发育和脏腑功能活动的是元气。  
            答案：C
            #示例三：
            题目：津液的丢失往往伴有气的损耗，说明二者的关系是  
            选项：A: 气能行津  B: 气能摄津  C: 气能生津  D: 津能生气  E: 津能载气  
            推理过程：津液为气的载体，气又能推动津液运行。津液过度丢失会导致气随津脱，体现了“津能载气”的关系。也就是说，津液是气的依附物，津损则气伤。  
            答案：E
            #请你参考以上思考方式，选出最佳答案。注意：最终输出只能为A、B、C、D、E中的一个，只返回答案字母选项，禁止返回其他内容。题目：{data["question"]}。选项：{str(data["options"])}

    '''
    match prompt_type:
        case 0:
            prompt = zero_shot_prompt
        case 1:
            prompt = few_shot_prompt
        case 2:
            prompt = cot_prompt
        case _:
            prompt = ""

    response = llm.chat(prompt)
    #print(response)
    # 直接匹配 A、B、C、D、E 五个选项（不区分大小写）
    extract_choice = re.compile(r".*?([A-Ea-e]).*", re.DOTALL)

    # 从 response 中提取第一个匹配的选项字母（转为大写）
    match = extract_choice.match(response)
    data["answer"] = match.group(1).upper() if match else ""

    return data