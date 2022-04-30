from model import *
import matplotlib.pyplot as plt
import base64
import connector.bigquery as bq

def get_model_list():

    models = bq.get_models()
    #get total parts required and compare with stock

    parts_used = {}
    for model in models:
        model.used = get_warn_status(model)
    return models

def get_warn_status(model):
    # DUMMY - 2 sells per week since we need the LSTM model
    parts_usage = {}
    total_parts = {}
    for part in model.parts:
        print(f'From part {part.part.name} on {model.name} we used {part.required}')
        
    return True if model.year < 2000 else False
def get_model_graph(id, sales):
    plt.clf()
    graphx = []
    graphy = []
    for row in sales:
        if row[0] == id:
            graphx.append(row[1])
            graphy.append(row[2])

    plt.plot(graphx, graphy)
    plt.savefig('graph.png')
    plt.clf()

    with open("graph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string
