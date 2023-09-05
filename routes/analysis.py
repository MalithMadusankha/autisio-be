from fastapi import APIRouter
from controller.analysis import sourece_detect
from models.analysis import Analysis

analysis = APIRouter()

@analysis.post('/airpolution')
async def find_analysis(analysis: Analysis):
    res = sourece_detect(analysis)
    print("res : ", res)
    return res
