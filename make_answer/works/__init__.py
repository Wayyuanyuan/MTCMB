from typing import Callable
from make_answer.chat.chat_invoker import ChatInvoker

from make_answer.works.TCM_ED_A import tcm_ed_a
from make_answer.works.TCM_ED_B import tcm_ed_b
from make_answer.works.TCM_FT_score import tcm_ft
from make_answer.works.TCMeEE_score import tcmeee
from make_answer.works.TCM_CHGD import tcm_chgd
from make_answer.works.TCM_LitData_score import tcm_litdata
from make_answer.works.TCM_MSDD import tcm_msdd
from make_answer.works.TCM_DiagData import tcm_diagdata
from make_answer.works.TCM_PR import tcm_pr
from make_answer.works.TCM_FRD import tcm_frd
from make_answer.works.drug_1 import drug_1
from make_answer.works.drug_2 import drug_2


question_prompt_dict: dict[str, Callable[[dict, ChatInvoker], dict]] = {
    "1": tcm_ed_a, "2": tcm_ed_b, "3": tcm_ft,"4": tcmeee, "5": tcm_chgd, "6": tcm_litdata,
    "7": tcm_msdd,"8": tcm_diagdata,"9":tcm_pr,"10": tcm_frd,"11": drug_1, "12":drug_2
}
