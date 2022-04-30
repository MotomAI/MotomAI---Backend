from google.cloud import bigquery
import random
from matplotlib.pyplot import prism
from model import *
client = bigquery.Client()
cached_parts ={}


def get_models():
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.modeldata_v2` LIMIT 20"""
    )
    models = []
    results = query_job.result()
    for model in results:
        models.append(Model(model["model_id"], model["name"], model["year"], model["brand"], [ Used_Part(Parts(part["reference_id"], None, part["cont_part"]), part['total_ref_used']) for part in model['references_used'] ], random.choice([True, False])))
    return models
    
