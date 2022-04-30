from fastapi import FastAPI

from statistics import mean

from get_model import get_model_graph, get_model_list, get_stock

from model import *
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


df = pd.read_csv('bq-results-20220430-091305-1651311205831.csv')
sales = df.values.tolist()

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

@app.get("/models/")
async def get_models():
    return get_model_list()

@app.get("/graph/{model}")
async def get_graph(model: int):
    return {"model": model, "graph": get_model_graph(model, sales)}

### DUMMY SECTION ###
dummy_parts = [Parts(1, "wheel", 12),Parts(2, "manillar", 2),Parts(3, "sillin", 4)]
dummy_models = [Model(1, " K 100 RS Motorsport   (1986-1988)", 1995, "BMW", [Used_Part(dummy_parts[0], 13),Used_Part(dummy_parts[1], 1)], True),
Model(id=1, name="Moto X (1986-1988)", year=1995, brand="Harly", parts=[Used_Part(dummy_parts[2], 1),Used_Part(dummy_parts[0], 1)], warn=False)]

fake_items_db = [{"model": "R 100 RT   (1978-1996)"}, {"model": "K 75 S Special   (1986-1988)"}, {"model": "R 100 RS   (1987-1995)"}]

@app.get("/stock/")
async def get_stocks():
    return get_stock()

def predict_week(id):
    graphy = []
    predicted_sales = 0

    for row in sales:
        if row[0] == id:
            graphy.append(row[2])

    for day in range(7):
        predicted_sales += mean(graphy[-7:])
        graphy.append(mean(graphy[-7:]))

    return predicted_sales
################################### // DUMMY ######################################
