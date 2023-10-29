from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Game(BaseModel):
    name: str
    game:str
    duration: int
    isWing: bool
    playOn: str
    _id: str
    