from fastapi import APIRouter
from controller.analysis import sourece_detect

analysis = APIRouter()

@analysis.post('/analysis')
async def find_analysis( ):
    res = sourece_detect()
    print("res : ", res)
    return res
