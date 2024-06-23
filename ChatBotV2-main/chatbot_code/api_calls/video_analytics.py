import requests
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

def video_log(api_parameters):
    data = {
        "name": api_parameters[0].lower()
    }
    response = requests.get(url= config["API"]["VIDEO_ANALYTICS_API"], params=data).json()
    if response['data'] is None:
        return response['message']
    else:
        print(type(response['data']))
        data = {key:[v for v in val.values()] for key, val in response['data'].items() if key in ['date_time', 'in_time(sec)', 'name']}
        return data
        # df = pd.DataFrame.from_dict(data)
        # print(df)
        # df.to_excel()