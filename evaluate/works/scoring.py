import json

import jieba
import sacrebleu
from bert_score import score
from loguru import logger
from rouge_chinese import Rouge


def bert_scoring(predictions: str, references: str):
    try:
        P, R, F1 = score(cands=[predictions], refs=[references], lang="zh", model_type='bert-base-chinese')
    except Exception:
        logger.exception("Bert score error")
        return 0
    return F1.mean().item()


def rouge1L_scoring(prediction: str, reference: str):
    # 创建 Rouge 对象
    rouge = Rouge()
    # 计算分数
    scores = rouge.get_scores(" ".join(jieba.cut(prediction)), " ".join(jieba.cut(reference)))

    return scores[0]["rouge-1"]["f"], scores[0]["rouge-l"]["f"]



def BLEU(prediction: str, reference: str):
    # 使用 jieba 分词
    prediction_tokens = ' '.join(jieba.cut(prediction))
    reference_tokens = ' '.join(jieba.cut(reference))

    # 使用 sacrebleu 计算 BLEU 分数
    bleu_score = sacrebleu.sentence_bleu(prediction_tokens, [reference_tokens])
    return bleu_score.score


def multiple_choice_score(prediction: list[str], reference: list[str]):
    """
    选择题得分计算，错选0分，漏选得到选对的分数
    :param prediction:
    :param reference:
    :return:
    """
    prediction = set(prediction)
    reference = set(reference)

    incorrect_choice = prediction - reference
    if len(incorrect_choice) != 0:
        return 0.0
    choice_less = reference - prediction
    return 1.0 - len(choice_less) / len(reference)


def judgement_correction_score(prediction: dict, reference: dict):
    pred_choice = set(prediction["answer"])
    ref_choice = set(reference["answer"])
    pred_reason = prediction["explanation"]
    ref_reason = reference["explanation"]
    if pred_choice != ref_choice:
        return 0.0
    bert=bert_scoring(pred_reason, ref_reason)
    rouge1, rougel = rouge1L_scoring(pred_reason, ref_reason)
    bleu=BLEU(pred_reason,ref_reason)
    return {"rouge1": rouge1, "rouge_l":rougel,"bert":bert,"bleu":bleu}
