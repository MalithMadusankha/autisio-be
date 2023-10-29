from models.game import Game
from schemas.serialize import serializeDict, serializeList
from config.db import db


def create(game: Game):
    print("<===== Create Game =====>")
    res = db.game.insert_one(dict(game))
    return {"status_code": 200, "detail": "Game Created"}

def getLast(game:str):
  print("<===== getLast =====>", game)
  filter = {"game": game}
#   dbres = db.game.find().sort([("_id", -1)])
  last_inserted_data = db.game.find_one(filter, sort=[("_id", -1)])

  print("dd ", last_inserted_data)
  res = serializeDict(last_inserted_data)
  print(res)
  return res


  