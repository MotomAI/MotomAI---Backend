from fastapi import FastAPI

app = FastAPI()


### DUMMY SECTION ###
fake_items_db = [{"model": "R 100 RT   (1978-1996)"}, {"model": "K 75 S Special   (1986-1988)"}, {"model": "R 100 RS   (1987-1995)"}]

@app.get("/warnings/")
async def get_warnings():
    return fake_items_db

@app.get("/infomodel/{model}")
async def get_model(model):
    return {"model": model, "used_parts": [{"part_id":13,"part_name":"wheel", "stock":12, "required":15}]}

@app.get("/stock/")
async def get_stock(page):
    return {"page": page,
            "used_parts": [{"part_id":95,"part_name":"moto chair", "stock":43}]
            }

################################### // DUMMY ######################################
