import requests
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def pdfapi(api_parameters):
    param = {
        "pdf_name": api_parameters[0]
    }
    response = requests.get(url = config["API"]["PDF_API"], params=param)
    return response.text