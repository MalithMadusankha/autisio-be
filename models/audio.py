from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Audio(BaseModel):
    name: str
    father:int
    mother: int
    playOn: str
    _id: str
    