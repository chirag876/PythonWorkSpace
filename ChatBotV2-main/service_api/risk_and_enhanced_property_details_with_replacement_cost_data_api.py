import requests

def risk_and_enhanced_property_details_with_replacement_cost_data(address, city, state, zip):
    try:
        PARAMS = {'address': address,
                  'city': city,
                  'state': state,
                  'zip': zip, 
            'Authorization': "Token token=zV6XdGTsVQzER3bU76Ny"
            }
        headers = {'Content-Type': 'application/json'}
        url = "https://api.hazardhub.com/v1/risks_and_enhanced_property_and_replacement_cost_data"
        response = requests.get(url, params = PARAMS, headers= headers).json()
        return response
    except:
        return "We are unable to process your request. Please try again in sometime"