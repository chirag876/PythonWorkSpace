import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def translation(api_parameters):
    param = {
        "lang_from": api_parameters[0],
        "text": api_parameters[1],
        "lang_to": api_parameters[2]
    }
    response = requests.get(url = config["API"]["TRANSLATION_API"], params= param)
    return response.text