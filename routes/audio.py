from fastapi import APIRouter
from controller.audio import create, getLastRespond
from models.audio import Audio

audio = APIRouter()

@audio.post('/audio')
async def createNew(audio: Audio):
    res = create(audio)
    print("res : ", res)
    return res

@audio.get('/audio')
async def get_last():
    audioLast = getLastRespond()
    return audioLast
