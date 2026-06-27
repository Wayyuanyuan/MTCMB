from typing import Callable

from make_answer.chat.chat_invoker import ChatInvoker

from make_answer.works.TCM_ED_A import tcm_ed_a
from make_answer.works.TCM_ED_B import tcm_ed_b
from make_answer.works.TCM_FT_score import tcm_ft
from make_answer.works.TCMeEE_score import tcmeee
from make_answer.works.TCM_CHGD import tcm_chgd
from make_answer.works.TCM_LitData_score import tcm_litdata
from make_answer.works.TCM_MSDD import tcm_msdd
from make_answer.works.TCM_Diagnosis import tcm_diagnosis
from make_answer.works.TCM_PR import tcm_pr
from make_answer.works.TCM_FRD import tcm_frd
from make_answer.works.TCM_SE_A import tcm_se_a
from make_answer.works.TCM_SE_B import tcm_se_b

question_prompt_dict: dict[str, Callable[[int, dict, ChatInvoker], dict]] = {
    "TCM-ED-A": tcm_ed_a,
    "TCM-ED-B": tcm_ed_b,
    "TCM-FT": tcm_ft,
    "TCMeEE": tcmeee,
    "TCM-CHGD": tcm_chgd,
    "TCM-LitData": tcm_litdata,
    "TCM-MSDD": tcm_msdd,
    "TCM-Diagnosis": tcm_diagnosis,
    "TCM-PR": tcm_pr,
    "TCM-FRD": tcm_frd,
    "TCM-SE-A": tcm_se_a,
    "TCM-SE-B": tcm_se_b,
}
