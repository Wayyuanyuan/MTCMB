from typing import Callable

from evaluate.works.TCM_SE_A import tcm_se_a
from evaluate.works.TCM_MSDD import tcm_msdd
from evaluate.works.TCM_PR import tcm_pr
from evaluate.works.exam import exam
from evaluate.works.TCM_FT_score import tcm_ft
from evaluate.works.TCMeEE_score import tcmeee
from evaluate.works.TCM_CHGD_score import tcm_chgd
from evaluate.works.TCM_LitData_score import tcm_litdata
from evaluate.works.TCM_Diagnosis import tcm_diagnosis
from evaluate.works.TCM_FRD import tcm_frd

question_standard_dict: dict[str, Callable[[str, str], dict | float]] = {
    "1": exam, "2": exam, "3": tcm_ft, "4": tcmeee, "5": tcm_chgd, "6": tcm_litdata,
    "7": tcm_msdd, "8": tcm_diagnosis, "9": tcm_pr, "10": tcm_frd, "11": tcm_se_a, "12": exam
}
