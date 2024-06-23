import os
import configparser

config = configparser.ConfigParser()
config.read('../chatbot_server/config.cfg')

def generate_pdf(api_params):
    filepath = config["PATH"]["FILES_PATH"]
    filename = os.path.basename(filepath)
    return filename

