from openai import OpenAI

def chat(msg:str):

    client = OpenAI(
        api_key="Input Your Key"
    )

    completion = client.chat.completions.create(
        model="glm-4-air-250414",
        messages=[
            {"role": "system", "content": "你是一名专业的中医教授，拥有专业的中医知识，你能够对中医学生回答的问题做出准确评价。"},
            {"role": "user","content": msg}
        ]
    )
    return completion.choices[0].message.content

def tcm_dc_a(standard_data: dict, llm_data: dict):
    prompt=f'''
        以下是一个中医填空题，包括题干、标准答案和学生回答。请你参考标准答案，从中医专业知识的角度，对学生回答进行打分。注意分数区间为[0，1]，只返回打分分数，不需要解释，禁止其他回答。
        题干为{standard_data["question"]},标准答案为{standard_data["answer"]},学生回答为{llm_data["answer"]}。请对上述学生回答进行打分，并返回打分分数。
'''
    score = chat(prompt)
    return score

