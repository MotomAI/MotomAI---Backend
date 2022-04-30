from fastapi import FastAPI

from model import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



dummy_parts = [Parts(1, "wheel", 12),Parts(2, "manillar", 2),Parts(3, "sillin", 4)]
dummy_models = [Model(1, " K 100 RS Motorsport   (1986-1988)", 1995, "BMW", [Used_Part(dummy_parts[0], 13),Used_Part(dummy_parts[1], 1)], True),
Model(id=1, name="Moto X (1986-1988)", year=1995, brand="Harly", parts=[Used_Part(dummy_parts[2], 1),Used_Part(dummy_parts[0], 1)], warn=False)]


### DUMMY SECTION ###
fake_items_db = [{"model": "R 100 RT   (1978-1996)"}, {"model": "K 75 S Special   (1986-1988)"}, {"model": "R 100 RS   (1987-1995)"}]

@app.get("/models/")
async def get_models():
    return dummy_models

@app.get("/infomodel/{model}")
async def get_model(model):
    return dummy_models[0]

@app.get("/stock/")
async def get_stock(page: int):
    return dummy_parts[1*page:1*page+10]

################################### // DUMMY ######################################
