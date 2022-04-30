from google.cloud import bigquery
import random
from google.oauth2 import service_account

from matplotlib.pyplot import prism
from model import *
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json', scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = bigquery.Client(credentials=credentials)
cached_parts ={}

def get_models_by_word(query):
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.modeldata_v2`  WHERE name LIKE '%{0}%' OR brand='{0}' LIMIT 20""".format(query)
    )
    models = []
    results = query_job.result()
    for model in results:
        models.append(Model(model["model_id"], model["name"], model["year"], model["brand"], [ Used_Part(Parts(part["reference_id"], None, part["cont_part"]), part['total_ref_used']) for part in model['references_used'] ], random.choice([True, False])))
    return models
    
def get_models():
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.modeldata_v2` LIMIT 20"""
    )
    models = {}
    results = query_job.result()
    for model in results:
        models[model["model_id"]] = Model(model["model_id"], model["name"], model["year"], model["brand"], [ Used_Part(Parts(part["reference_id"], None, part["cont_part"]), part['total_ref_used']) for part in model['references_used'] ], False)
    return models
    
def get_stock():
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.warehouse_v3` """
    )
    stock = {}
    results = query_job.result()
    for part in results:
        stock[part["reference_id"]] = part["cont_part"]
    return stock