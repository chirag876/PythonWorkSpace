from flask import Flask, jsonify, request, send_file
import requests
from Swagger_config.swagger_configuration import configure_swagger, serve_swagger_json, SWAGGER_URL

app = Flask(__name__)

swaggerui_blueprint = configure_swagger()
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    return serve_swagger_json()

@app.route('/documents', methods=['GET'])
def get_documents():
    sharepoint_url = 'https://abc.sharepoint.com/sites/AzurePowerApps/_api/web/lists/getByTitle(PDF_Details_List)/items'
    headers = {'Accept': 'application/json;odata=verbose'}
    try:
        response = requests.get(sharepoint_url, headers=headers, verify=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        documents = []
        for item in data['d']['results']:
            document = {
                'title': item['Title'],
                # 'url': item['File']['ServerRelativeUrl'],
                # 'modified': item['Modified'],
                # 'modified_by': item['Editor']['Title'],
                # 'path': item['File']['ServerRelativeUrl'],  # Assuming 'Path' is the server-relative URL
                # 'add_column': item['AddColumn'] if 'AddColumn' in item else None  # Handle missing 'AddColumn' field
            }
            documents.append(document)
        return jsonify({'documents': documents})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})
    except ValueError as ve:
        return jsonify({'error': 'Invalid JSON response from SharePoint API'})

# SharePoint API Endpoint
SHAREPOINT_URL = "https://{your-sharepoint-site}/_api/web/lists/getbytitle('{list-name}')/items"



# Route to download file
@app.route('/download-file', methods=['GET'])
def download_file():


    # Get file name from request
    file_name = request.args.get('file_name')

    # Query SharePoint to retrieve file information
    response = requests.get(SHAREPOINT_URL, params={"$filter": f"FileLeafRef eq '{file_name}'"})
    
    try:
        # Extract file URL from response
        file_url = response.json()["d"]["results"][0]["FileRef"]
        
        # Download the file
        file_response = requests.get(file_url)
        
        # Return file content as response
        return send_file(file_response.content, as_attachment=True)
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True, port=8000)
