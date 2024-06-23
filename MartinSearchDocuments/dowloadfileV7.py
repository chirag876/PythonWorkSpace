from flask import Flask, request, jsonify
import requests
import certifi  # Importing certifi for CA certificate path

app = Flask(__name__)

# Constants (replace placeholders with actual values)
TENANT_ID = 'd6881518-0d5-bc4f-fd091c3b1889'
CLIENT_ID = 'ab141f71-dfa-acc4-a2031341ec30'
CLIENT_SECRET = '.fA8Q~qapgO42xk7L6pkkgdlishntVkc.W'
RESOURCE = 'https://abc.sharepoint.com'
AUTHORITY_URL = 'https://login.microsoftonline.com/' + TENANT_ID
TOKEN_ENDPOINT = f'{AUTHORITY_URL}/oauth2/v2.0/token'
SHAREPOINT_SITE_URL = 'https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/'

def get_access_token():
    """Function to retrieve an access token from Azure AD."""
    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'  # Using Microsoft Graph scope
    }
    response = requests.post(token_url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Failed to obtain token: {response.status_code}, {response.text}")
        return None

@app.route('/search_pdf', methods=['GET'])
def search_pdf():
    """Endpoint to search for PDF files in SharePoint based on a query."""
    query = request.args.get('query', '')
    access_token = get_access_token()
    if not access_token:
        return jsonify({'message': 'Failed to authenticate with Azure AD'}), 401

    pdf_url = search_sharepoint(query, access_token)
    if pdf_url:
        return jsonify({'url': pdf_url}), 200
    else:
        return jsonify({'message': 'PDF not found'}), 404

def search_sharepoint(query, access_token):
    """Function to perform the search query on SharePoint and return the first PDF URL found."""
    headers = {'Authorization': f'Bearer {access_token}', 'Accept': 'application/json;odata=verbose'}
    search_url = f"{SHAREPOINT_SITE_URL}/_api/search/query?querytext='filetype:pdf AND {query}'&rowlimit=10&selectproperties='Path'"
    response = requests.get(search_url, headers=headers, verify=certifi.where())
    if response.status_code == 200:
        try:
            results = response.json()
            paths = [cell['Value'] for result in results['d']['query']['PrimaryQueryResult']['RelevantResults']['Table']['Rows'] for cell in result['Cells'] if cell['Key'] == 'Path' and cell['Value'].endswith('.pdf')]
            if paths:
                return paths[0]  # Return the first PDF URL found
            else:
                print("No PDF paths found in the response.")
        except KeyError as e:
            print(f"Error parsing response: {e}")
    else:
        print(f"Unexpected status code from SharePoint: {response.status_code}, {response.text}")
    return None

if __name__ == '__main__':
    app.run(debug=True, port=8000)