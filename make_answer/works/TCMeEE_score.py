from make_answer.chat.chat_invoker import ChatInvoker


def tcmeee(prompt_type:int,data: dict, llm: ChatInvoker) -> dict:
    zero_shot_prompt = f'''请严格按照中医标准术语，从下列医案中精准提取信息，并生成结构化JSON数据。表单如下：
    ##表单内容
    Symptoms：症状。
    Disease Name：西医病名。
    TCM Disease Name：中医病名。
    TCM Pattern：中医证型。
    Cause and Mechanism of Disease：病因病机。
    Method of Treatment：治法。
    Formulas：方剂名。
    Medicinals：药物组成。不需要给出剂量。
    ##注意
    1.若医案中未涉及相关内容，请填充“无”。
    2.禁用口语化表达，严格使用医学专业表达。
    3.输出格式与信息抽取的表单一致，不要输出其它格式，禁用markdown格式。
    4.表项用字符串形式，不需要数组格式
    请从以下医案中提取信息，完成上述表单：{data["Medical_case"]}
'''
    few_shot_prompt = f'''
        请严格按照中医标准术语，从下列医案中精准提取信息，并生成结构化JSON数据。表单如下：
        ##表单内容
        Symptoms：症状。
        Disease Name：西医病名。
        TCM Disease Name：中医病名。
        TCM Pattern：中医证型。
        Cause and Mechanism of Disease：病因病机。
        Method of Treatment：治法。
        Formulas：方剂名。
        Medicinals：药物组成。不需要给出剂量。
        ##注意
        1.若医案中未涉及相关内容，请填充“无”。
        2.禁用口语化表达，严格使用医学专业表达。
        3.输出格式与信息抽取的表单一致，不要输出其它格式，禁用markdown格式。
        4.表项用字符串形式，不需要数组格式
        ##请参考以下示例：
        【示例一】
        1.医案：出处：临证指南医案。正文：某（二一）脉细弱，自汗体冷，形神疲瘁，知饥少纳，肢节痠楚。病在营卫，当以甘温。生黄芪 桂枝木 白芍 炙草 煨姜 南枣
        2.答案：
        "Symptoms": "脉细弱；自汗；体冷；形神疲瘁；知饥少纳；肢节痠楚",
        "Disease Name": "无",
        "TCM Disease Name": "营卫不和",
        "TCM Pattern": "营卫不和，阳气不足",
        "Cause and Mechanism of Disease": "营卫不和，阳气不足，不能温养",
        "Method of Treatment": "甘温调和营卫，益气固表",
        "Formulas": "无",
        "Medicinals": "生黄芪；桂枝木；白芍；炙草；煨姜；南枣"
        【示例二】
        1.医案：出处：《孔伯华医案》，主诉：又复发颐，大便燥秘，脉象洪数。
        2.答案：
        "Symptoms": "发颐；大便燥秘；脉象洪数",
        "Disease Name": "无",
        "TCM Disease Name": "发颐",
        "TCM Pattern": "胃热上蒸",
        "Cause and Mechanism of Disease": "热毒蕴结，阳明热盛，津液受损",
        "Method of Treatment": "清热解毒，通腑泄热",
        "Formulas": "无",
        "Medicinals": "无"
        【示例三】
        1.医案：出处：幼科医验，正文：一儿，伤食作泻，肚腹膨胀。新会皮 柴胡 莱菔子 楂肉 防风 芍药 猪苓 建泽泻 赤茯苓 麦芽 车前
        2.答案：
        "Symptoms": "伤食作泻，肚腹膨胀",
        "Disease Name": "无",
        "TCM Disease Name": "伤食泻",
        "TCM Pattern": "食积气滞",
        "Cause and Mechanism of Disease": "饮食不节损伤脾胃，食积内停，气机阻滞，运化失职，清浊不分，水湿下注",
        "Method of Treatment": "消食导滞，理气和中",
        "Formulas": "无",
        "Medicinals": "新会皮,柴胡,莱菔子,楂肉,防风,芍药,猪苓,建泽泻,赤茯苓,麦芽,车前"
        #请你参考以上思考方式，从以下医案中提取信息，完成上述表单：{data["Medical_case"]}
'''
    cot_prompt = f'''
    请严格按照中医标准术语，从下列医案中精准提取信息，并生成结构化JSON数据。表单如下：
    ##表单内容
    Symptoms：症状。
    Disease Name：西医病名。
    TCM Disease Name：中医病名。
    TCM Pattern：中医证型。
    Cause and Mechanism of Disease：病因病机。
    Method of Treatment：治法。
    Formulas：方剂名。
    Medicinals：药物组成。不需要给出剂量。
    ##注意
    1.若医案中未涉及相关内容，请填充“无”。
    2.禁用口语化表达，严格使用医学专业表达。
    3.输出格式与信息抽取的表单一致，不要输出其它格式，禁用markdown格式。
    4.表项用字符串形式，不需要数组格式
    ##请参考以下示例及其推理过程：
    【示例一】
    1.医案：出处：临证指南医案。正文：某（二一）脉细弱，自汗体冷，形神疲瘁，知饥少纳，肢节痠楚。病在营卫，当以甘温。生黄芪 桂枝木 白芍 炙草 煨姜 南枣
    2.推理过程：
    症状（Symptoms）：脉细弱、自汗、体冷、形神疲瘁、知饥少纳、肢节痠楚。
    从原文中可以看到具体的症状描述，因此提取出这些症状。
    西医病名（Disease Name）：无。
    医案中没有提到西医病名，填“无”。
    中医病名（TCM Disease Name）：营卫不和。
    根据病在营卫这一描述，可以推测病名为“营卫不和”。
    中医证型（TCM Pattern）：营卫不和，阳气不足。
    根据病在营卫及甘温治疗的描述，可以推测证型为“营卫不和，阳气不足”。
    病因病机（Cause and Mechanism of Disease）：营卫不和，阳气不足，不能温养。
    提到病在营卫，阳气不足，因此病因病机为“营卫不和，阳气不足，不能温养”。
    治法（Method of Treatment）：甘温调和营卫，益气固表。
    根据“当以甘温”治疗可推测为甘温调和营卫，益气固表。
    方剂名（Formulas）：无。
    医案中没有提到方剂，填“无”。
    药物组成（Medicinals）：生黄芪、桂枝木、白芍、炙草、煨姜、南枣。
    根据文中提到的药物，直接提取。
    【示例二】
    1.医案：出处：《孔伯华医案》，主诉：又复发颐，大便燥秘，脉象洪数。
    2.推理过程：
    症状（Symptoms）：发颐、大便燥秘、脉象洪数。
    原文直接给出症状，提取完整症状。
    西医病名（Disease Name）：无。
    原文没有提到西医病名，填“无”。
    中医病名（TCM Disease Name）：发颐。
    根据“发颐”这一描述，病名为“发颐”。
    中医证型（TCM Pattern）：胃热上蒸。
    根据大便燥秘和脉象洪数的描述，可推测为胃热上蒸证型。
    病因病机（Cause and Mechanism of Disease）：热毒蕴结，阳明热盛，津液受损。
    “热毒蕴结，阳明热盛，津液受损”符合该症状的病因机理。
    治法（Method of Treatment）：清热解毒，通腑泄热。
    提到治疗方法为清热解毒和通腑泄热。
    方剂名（Formulas）：无。
    没有提到方剂，填“无”。
    药物组成（Medicinals）：无。
    没有提到具体药物，填“无”。
    【示例三】
    1.医案：出处：幼科医验，正文：一儿，伤食作泻，肚腹膨胀。新会皮 柴胡 莱菔子 楂肉 防风 芍药 猪苓 建泽泻 赤茯苓 麦芽 车前
    2.推理过程：
    症状（Symptoms）：伤食作泻，肚腹膨胀。
    这直接来自原文“伤食作泻，肚腹膨胀”，因此症状为“伤食作泻，肚腹膨胀”。
    西医病名（Disease Name）：无。
    医案中并未涉及西医病名，因此填“无”。
    中医病名（TCM Disease Name）：伤食泻。
    根据“伤食作泻”的症状判断，属于“伤食泻”这一中医病名。
    中医证型（TCM Pattern）：食积气滞。
    伤食所导致的泻病通常属于食积气滞，反映出脾胃受损，气滞导致的腹泻。
    病因病机（Cause and Mechanism of Disease）：饮食不节损伤脾胃，食积内停，气机阻滞，运化失职，清浊不分，水湿下注。
    伤食导致的病因病机一般为饮食不节，损伤脾胃，食物积滞，气机阻滞，水湿下注，导致泻病。
    治法（Method of Treatment）：消食导滞，理气和中。
    治疗方法应以消食导滞为主，理气和中，疏通积滞。
    方剂名（Formulas）：无。
    原文未提到具体的方剂，填“无”。
    药物组成（Medicinals）：新会皮,柴胡,莱菔子,楂肉,防风,芍药,猪苓,建泽泻,赤茯苓,麦芽,车前。
    这些药物组成直接来自原文列举的药物。
    #请你参考以上思考方式，从以下医案中提取信息，完成上述表单：{data["Medical_case"]}
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
    data["answer"] = response

    return data
