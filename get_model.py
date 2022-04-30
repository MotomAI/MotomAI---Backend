from model import *
import matplotlib.pyplot as plt
import base64
import connector.bigquery as bq

def get_model_list():

    models = bq.get_models()
    
    return models

def get_stock():
    return bq.get_stock()
def get_warn_status(model, parts_usage, total_parts):
# DUMMY - 2 sells per week since we need the LSTM model
    parts_usage[model.id] = set()
    for part in model.parts:
        parts_usage[model.id].add(part.part.id)
        if part.part.id  not in total_parts:
            total_parts[part.part.id] = part.required
        else:
            total_parts[part.part.id] += part.required

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
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.savefig('graph.png')
    plt.clf()

    with open("graph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string
