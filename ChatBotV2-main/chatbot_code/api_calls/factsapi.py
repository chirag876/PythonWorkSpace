import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def facts(api_parameters):
    param = {
        "limit": api_parameters[0]
    }

    response = requests.get(url = config["API"]["FACTS_API"], params= param)
    return response.text