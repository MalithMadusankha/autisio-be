from fastapi import HTTPException
from typing import List, Dict
from models.audio import Audio
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId


def create(audio: Audio):
    print("<===== Create Audio =====>")
    res = db.audio.insert_one(dict(audio))
    return {"status_code": 200, "detail": "Audio Created"}

def getLastRespond():
    print("<===== getLast =====>")
    res = serializeList(db.audio.find().sort([("_id", -1)]).limit(1))
    print(res)
    return res

  