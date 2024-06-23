import requests

def facts(limit):
    try:
        #limit = 3
        #api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
        PARAMS = {'limit': limit}
        api_url = 'https://api.api-ninjas.com/v1/facts'
        response = requests.get(api_url, params = PARAMS, headers={'X-Api-Key': 'hwqtjleCWClx2An+==wdpBc7jQG5'})
        if response.status_code == requests.codes.ok:
            return response.text
            #fact = response['fact']
            #return response.json(fact)
        else:
            return "Error:", response.status_code, response.text

    except:
        return "We are unable to process your request. Please try again in sometime"