import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def risk_and_enhanced_property_details(api_parameters):
    param = {
        "address": api_parameters[0],
        "city": api_parameters[1],
        "state": api_parameters[2],
        "zip": api_parameters[3]
    }

    response = requests.get(url = config["API"]["RISK_AND_ENHANCED_PROPERTY_DETAILS"], params= param)
    return response.text