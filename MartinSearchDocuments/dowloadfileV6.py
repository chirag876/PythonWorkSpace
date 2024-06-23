import requests
import json

# Microsoft Graph API endpoints
graph_url = "https://graph.microsoft.com/v1.0"
tenant_id = 'd688159-4bd5-bc4f-fd091c3b1889'
client_id = 'ab141ee-4dfa-acc4-a2031341ec30'
client_secret = '.fQ8pqcVapgO42xk7L6pkkgdlishntVkc.W'
site_id = 'https://abc.sharepoint.com/sites/AzurePowerApps/'

# Get access token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
token_data = {
    'client_id': client_id,
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# Get files from document library
library_url = f"{graph_url}/sites/{site_id}/lists/Sample_PDF/items"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
files_response = requests.get(library_url, headers=headers)

# Check if the request was successful
if files_response.status_code != 200:
    print(f"Failed to retrieve files. Status code: {files_response.status_code}")
    print(files_response.text)
    exit()  # Exit the script if there's an error

files_data = files_response.json()

# Check if the response contains items
if 'value' in files_data:
    # Download files
    for file_item in files_data['value']:
        file_name = file_item['name']
        file_url = file_item['@microsoft.graph.downloadUrl']
        print(f"Downloading file: {file_name} from {file_url}")
        file_download_response = requests.get(file_url, headers=headers)
        
        # Check if the download was successful
        if file_download_response.status_code == 200:
            # Save the file
            with open(file_name, 'wb') as file:
                file.write(file_download_response.content)
                print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download file: {file_name}. Status code: {file_download_response.status_code}")
else:
    print("No files found in the document library.")