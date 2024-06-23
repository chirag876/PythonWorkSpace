import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def hazard_hub(api_parameters):
    param = {
        "data": api_parameters[0]
    }

    response = requests.get(url = config["API"]["HAZARD_HUB"], params= param)
    return response.text