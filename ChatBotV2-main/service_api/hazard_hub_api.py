# For Risk and Enhanced property details with Replacement cost data
# https://api.hazardhub.com/v1/risks_and_enhanced_property_and_replacement_cost_data?address=" + _request.address + "&city=" + _request.city + "&state=" + _request.state + "&zip=" + _request.zip

import requests
import rater_api

def hazard_hub(data):
    try:
        headers = {'Authorization': 'Token token='}
        url = "https://api.hazardhub.com/v1/risks_and_enhanced_property_and_replacement_cost_data"
        response = requests.get(url, data= data, headers= headers).json()
        #print(data)
        #print(response)
        rater = rater_api.rater()
        print(rater)
        return f'Address verified successfully Calling rater API \n {rater}'
    except:
        return "We are unable to process your request. Please try again in sometime"