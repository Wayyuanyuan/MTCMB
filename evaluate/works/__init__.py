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

question_standard_dict: dict[str, Callable] = {
    "TCM-ED-A": exam,
    "TCM-ED-B": exam,
    "TCM-FT": tcm_ft,
    "TCMeEE": tcmeee,
    "TCM-CHGD": tcm_chgd,
    "TCM-LitData": tcm_litdata,
    "TCM-MSDD": tcm_msdd,
    "TCM-Diagnosis": tcm_diagnosis,
    "TCM-PR": tcm_pr,
    "TCM-FRD": tcm_frd,
    "TCM-SE-A": tcm_se_a,
    "TCM-SE-B": exam,
}
