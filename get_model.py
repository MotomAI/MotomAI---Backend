from joblib import PrintTime
from model import *
import matplotlib.pyplot as plt
import base64
from statistics import mean
import connector.bigquery as bq
import random
def get_model_list_by_word(query):
    models = bq.get_models_by_word(query)
    return models

def predict_week(id, sales):
    graphy = []
    predicted_sales = 0

    for row in sales:
        if row[0] == id:
            graphy.append(row[2])

    for day in range(7):
        predicted_sales += mean(graphy[-7:])
        graphy.append(mean(graphy[-7:]))

    return int(predicted_sales)

def get_model_list(sales):

    models = bq.get_models()
    #get total parts required and compare with stock
    stocks = bq.get_stock()
    parts_usage_percent = {} # {model_id: {part_id: usage_percent}}
    required_parts = {}
    models_warned = set()
    models_that_use_parts = {} # {part_id: [model_id]}
    for model in models:
        parts_usage_percent = {}
        total = sum ([ part.required for part in models[model].parts ])
        for part in models[model].parts:
            parts_usage_percent[part.part.id] = part.required / total * 100
        
        for part in random.choices(list(parts_usage_percent.keys()), weights=list(parts_usage_percent.values()), k=predict_week(model, sales)) :
            if part in required_parts:
                required_parts[part] += 1
                models_that_use_parts[part].add(model)
                if  required_parts[part] > stocks[part]:
                    for model_id in models_that_use_parts[part]:
                        models_warned.add(model_id)
                        models[model_id].warn = True
            else:
                required_parts[part] = 1 
                models_that_use_parts[part] = {model}
    
    # for part in required_parts:
    #     if part > stocks[part]:
    #         for model_id in models_that_use_parts[part]:
    #             models_warned.add(model_id)
    #             models[model_id].warn = True

    return {'total_warns': len(models_warned), 'models': models}


def get_warn_status(model, parts_usage, total_parts):
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
def get_stock():
    return bq.get_stock()