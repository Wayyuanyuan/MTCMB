def exam(standard_data: dict, llm_data: dict) -> float:
    score = 0
    choice = llm_data["answer"]
    if choice != "" and choice.lower() == standard_data["answer"].lower():
        score = 1

    return score