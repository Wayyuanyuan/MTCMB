from evaluate.works.scoring import bert_scoring


def _text_field(record: dict, *keys: str) -> str:
    for key in keys:
        val = record.get(key)
        if val is not None and str(val).strip():
            return str(val).strip()
    return ""


def tcm_ft(standard_data: dict, llm_data: dict) -> dict:
    response = _text_field(llm_data, "points", "answer")
    reference = _text_field(standard_data, "points", "answer")
    bert = bert_scoring(response, reference)
    return {"bert": bert}
