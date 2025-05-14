from evaluate.works.scoring import  bert_scoring


def tcm_ft(standard_data: dict, llm_data: dict) -> float:
    response = llm_data["answer"]
    bert = bert_scoring(response, standard_data["answer"])

    return bert