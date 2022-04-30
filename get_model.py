from model import *
def get_model(model_id):
    """
    Some information will be retrieved from versions table: id, name, year.
    The required parts for this model will be calculated thnx to the historical values * prediction amount sales
    """

    # DUMMY - 10 models per week since we need the LSTM model
    