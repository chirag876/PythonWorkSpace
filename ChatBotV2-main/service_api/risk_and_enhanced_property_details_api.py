import requests

def risk_and_enhanced_property_details(address, city, state, zip):
    try:
        PARAMS = {'address': address,
                  'city': city,
                  'state': state,
                  'zip': zip, 
            'key': "zV6XdGTsVQzER3bU76Ny"
            }
        headers = {'Content-Type': 'application/json'}
        url = "https://api.hazardhub.com/v1/risks_and_enhanced_property"
        response = requests.get(url, params = PARAMS, headers= headers).json()
        return response 
    except:
        return "We are unable to process your request. Please try again in sometime"