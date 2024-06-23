import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def rater():
    response = requests.get(url = config["API"]["RATER"])
    return response.text