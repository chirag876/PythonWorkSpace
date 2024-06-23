import requests
from flask import Flask, send_file
from urllib.parse import quote

app = Flask(__name__)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Encode the filename for use in the URL
    encoded_filename = quote(filename)
    
    # Construct the SharePoint URL for the file
    sharepoint_url = f'https://abc.sharepoint.com/sites/AzurePowerApps/abc/{encoded_filename}'
    
    # Fetch the file from the SharePoint URL
    response = requests.get(sharepoint_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Send the file as a response
        return send_file(response.content, as_attachment=True, attachment_filename=filename)
    else:
        return f"File '{filename}' not found or unable to download.", 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
