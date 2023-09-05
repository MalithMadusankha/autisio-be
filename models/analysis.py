from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Analysis(BaseModel):
    game_1: float
    game_2: float
    game_3: float
    game_4: float
    _id: str
    