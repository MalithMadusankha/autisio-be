from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes.analysis import source

app = FastAPI()

previous_val = "None"

origins = [
    "exp://192.168.1.2:19000",
    "http://192.168.1.2:19000"
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.0.100:19006",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(source)

print("<============== Server started ==============>")

@app.get('/')
async def index():
    return {"message": "Welcome to Air Polution Server !!!"}

