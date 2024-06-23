import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def weather(api_parameters):
    param = {
        "city_name": api_parameters[0]
    }
    response = requests.get(url = config["API"]["WEATHER_API"], params= param)
    return response.text
