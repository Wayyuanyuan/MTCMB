from evaluate.works.scoring import rouge1L_scoring, bert_scoring, BLEU


def tcm_litdata(standard_data: dict, llm_data: dict) -> dict:
    rouge1_avg = 0
    rougel_avg = 0
    #bert_avg = 0
    bleu_avg=0

    for index, question in enumerate(standard_data["annotations"]):
        response = llm_data["annotations"][index]["A"]
        if response.strip() == "" or question["A"] == "":
            continue
        rouge1, rougel = rouge1L_scoring(response, question["A"])
        #bert = bert_scoring(response, question["A"])
        bleu=BLEU(response,question["A"])
        rouge1_avg += rouge1
        rougel_avg += rougel
        #bert_avg += bert
        bleu_avg+=bleu

    rouge1_avg /= len(standard_data["annotations"])
    rougel_avg /= len(standard_data["annotations"])
    #bert_avg /= len(standard_data["annotations"])
    bleu_avg /= len(standard_data["annotations"])

    #return {"rouge_1": rouge1_avg, "rouge_l": rougel_avg, "bert": bert_avg,"bleu":bleu_avg}
    return {"rouge_1": rouge1_avg, "rouge_l": rougel_avg,  "bleu": bleu_avg}
