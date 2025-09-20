import json
from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU


def tcmeee(standard_data: dict, llm_data: dict) -> dict:
    response = json.dumps(llm_data["answer"], ensure_ascii=False)
    answer = json.dumps(standard_data["answer"], ensure_ascii=False)

    if answer == "" or response == "":
        return {"rouge_1": 0.0, "rouge_l": 0.0, "bert": 0.0,"bleu": 0.0}
    rouge_1, rouge_l = rouge1L_scoring(response, answer)
    bert = bert_scoring(response, answer)
    bleu=BLEU(response, answer)

    return {"rouge_1": rouge_1, "rouge_l": rouge_l, "bert": bert,"bleu":bleu}
