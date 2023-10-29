from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Analysis(BaseModel):
    focused: float
    selectiv: float
    divided: float
    sustained: float
    father: float
    mother: float
    _id: str
    