import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def timezone(api_parameters):
    param = {
        "city_name": api_parameters[0]
    }
    response = requests.get(url = config["API"]["TIMEZONE_API"], params= param)
    return response.text