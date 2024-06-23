# import requests
# from flask import Flask, send_file
# import mimetypes

# app = Flask(__name__)

# # Define the directory where your SharePoint files are stored
# SHAREPOINT_SITE_URL = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/"
# SHAREPOINT_LIST_NAME = "PDF_Details_List"  # Replace with your list name


# def get_sharepoint_file_content(filename):
#     try:
#         # Fetch the file content using Microsoft Graph API
#         file_url = f"{SHAREPOINT_SITE_URL}/_api/web/lists/getbytitle('{SHAREPOINT_LIST_NAME}')/items?$filter=Title eq '{filename}'"
#         file_response = requests.get(file_url)
#         file_data = file_response.json()

#         if file_data.get("d").get("results"):
#             # Retrieve the file content (assuming it's stored in a field named 'Title')
#             file_content = file_data.get("d").get("results")[0].get("Title")
#             return file_content
#         else:
#             print(f"File '{filename}' not found in SharePoint.")
#             return None
#     except Exception as e:
#         print(f"Error retrieving file from SharePoint: {e}")
#         return None
            


# def get_file_mime_type(filename):
#     # Get the MIME type based on the file extension
#     mime_type, _ = mimetypes.guess_type(filename)
#     return mime_type

# @app.route("/download/<filename>")
# def download_sharepoint_file(filename):
#     # Get the file content from SharePoint (replace with your actual logic)
#     file_content = get_sharepoint_file_content(filename)

#     if file_content:
#         # Get the MIME type of the file
#         mime_type = get_file_mime_type(filename)
#         # Serve the file for download
#         return send_file(
#             file_content,
#             as_attachment=True,
#             attachment_filename=filename,
#             mimetype=mime_type if mime_type else "application/octet-stream",
#         )
#     else:
#         return f"File '{filename}' not found in SharePoint."

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

import requests
from flask import Flask, send_file
import mimetypes
import os

app = Flask(__name__)

# Define the directory where your SharePoint files are stored
SHAREPOINT_SITE_URL = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/"
SHAREPOINT_LIST_NAME = "PDF_Details_List"  # Replace with your list name


def get_sharepoint_file_content(filename):
    try:
        # Construct the URL to fetch the file by filename
        file_url = f"{SHAREPOINT_SITE_URL}/_api/web/lists/getbytitle('{SHAREPOINT_LIST_NAME}')/items?$filter=Title eq '{filename}'"
        
        # Make the API request to SharePoint
        headers = {
            'Content-Type': 'application/json;odata=verbose',
            'Accept': 'application/json;odata=verbose'
        }
        file_response = requests.get(file_url, headers=headers)
        file_data = file_response.json()
        print(file_data)

        if file_data.get("d").get("results"):
            # Retrieve the file content URL
            file_content = file_data.get("d").get("results")[0].get("File").get("ServerRelativeUrl")
            return file_content
        else:
            print(f"File '{filename}' not found in SharePoint.")
            return None
    except Exception as e:
        print(f"Error retrieving file from SharePoint: {e}")
        return None


def download_sharepoint_file(filename):
    # Get the file content from SharePoint
    file_url = get_sharepoint_file_content(filename)
    print(file_url, filename)

    if file_url:
        # Download the file locally
        local_file_path = os.path.join(os.getcwd(), filename)
        response = requests.get(f"{SHAREPOINT_SITE_URL}{file_url}", stream=True)
        with open(local_file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        return local_file_path
    else:
        return None


@app.route("/download/<filename>")
def serve_file(filename):
    # Download the file from SharePoint
    file_path = download_sharepoint_file(filename)

    if file_path:
        # Get the MIME type of the file
        mime_type, _ = mimetypes.guess_type(filename)

        # Serve the file for download
        return send_file(
            file_path,
            as_attachment=True,
            attachment_filename=filename,
            mimetype=mime_type if mime_type else "application/octet-stream",
        )
    else:
        return f"File '{filename}' not found in SharePoint."


if __name__ == "__main__":
    app.run(debug=True, port=8000)
