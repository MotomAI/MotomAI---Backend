from google.cloud import bigquery
import random
from matplotlib.pyplot import prism
from model import *
client = bigquery.Client()
cached_parts ={}
# def get_part(part_id):
#     if part_id is not cached_parts:
#         print("A")
#         query_job = client.query(
#         """
#         SELECT * FROM `bot-testing-345117.hackupcglobal.warehouse` WHERE reference_id = {} LIMIT 1""".format(part_id)
#         )
#         results = query_job.result()
#         for part in results:
#             cached_parts[part_id] = Parts(part["reference_id"], None, part["cont_part"])
#     return cached_parts[part_id]

def get_models():
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.modeldata_v2` LIMIT 10"""
    )
    models = []
    results = query_job.result()
    for model in results:
        models.append(Model(model["model_id"], model["name"], model["year"], model["brand"], [ Used_Part(Parts(part["reference_id"], None, part["cont_part"]), part['total_ref_used']) for part in model['references_used'] ], random.choice([True, False])))
    return models
    
