from google.cloud import bigquery

from matplotlib.pyplot import prism
from model import *
client = bigquery.Client()
def get_models():
    query_job = client.query(
    """
    SELECT * FROM `bot-testing-345117.hackupc2022.model_data` LIMIT 20"""
    )
    models = []
    results = query_job.result()
    for model in results:
        models.append(Model(model.model_id, model.name, model.year, model.brand, [Used_Part(part['reference_id'], part['total_ref_used']) for part in model.references_used], False	))
    return models
    
