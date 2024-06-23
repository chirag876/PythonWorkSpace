import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def risk_and_enhanced_property_details_with_replacement_cost_data(api_parameters):
    param = {
        "address": api_parameters[0],
        "city": api_parameters[1],
        "state": api_parameters[2],
        "zip": api_parameters[3]
    }

    response = requests.get(url = config["API"]["RISK_AND_ENHANCED_PROPERTY_DETAILS_WITH_REPLACEMENT_COST_DATA"], params= param)
    return response.text