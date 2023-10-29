from fastapi import APIRouter
from controller.game import create, getLast
from models.game import Game

game = APIRouter()

@game.post('/game')
async def createNew(game: Game):
    res = create(game)
    print("res : ", res)
    return res

@game.get('/game/{game}')
async def get_last(game:str):
    print(" get_last ==========", game)
    gameLast = getLast(game)
    return gameLast
