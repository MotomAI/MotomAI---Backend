from fastapi import FastAPI
import connector.bigquery as bq
import matplotlib.pyplot as plt
import base64

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



dummy_parts = [Parts(1, "wheel", 12),Parts(2, "manillar", 2),Parts(3, "sillin", 4)]
dummy_models = [Model(1, " K 100 RS Motorsport   (1986-1988)", 1995, "BMW", [Used_Part(dummy_parts[0], 13),Used_Part(dummy_parts[1], 1)], True),
Model(id=1, name="Moto X (1986-1988)", year=1995, brand="Harly", parts=[Used_Part(dummy_parts[2], 1),Used_Part(dummy_parts[0], 1)], warn=False)]


### DUMMY SECTION ###
fake_items_db = [{"model": "R 100 RT   (1978-1996)"}, {"model": "K 75 S Special   (1986-1988)"}, {"model": "R 100 RS   (1987-1995)"}]

@app.get("/models/")
async def get_models():
    return bq.get_models()

@app.get("/infomodel/{model}")
async def get_model(model: int):
    graph = get_graph(model)
    model = Model(id=1, name="Moto X (1986-1988)", year=1995, brand="Harly", parts=[Used_Part(dummy_parts[2], 1),Used_Part(dummy_parts[0], 1)], warn=False, graph=graph)
    return model

@app.get("/stock/")
async def get_stock(page: int):
    return dummy_parts[1*page:1*page+10]

################################### // DUMMY ######################################

def get_graph(id):
    graphx = []
    graphy = []
    for row in sales:
        if row[0] == id:
            graphx.append(row[1])
            graphy.append(row[2])

    plt.plot(graphx, graphy)
    plt.savefig('graph.png')
    with open("graph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string
