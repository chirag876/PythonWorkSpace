# import requests
# from flask import Flask, send_file
# import mimetypes

# app = Flask(__name__)

# # Define the directory where your SharePoint files are stored
# SHAREPOINT_SITE_URL = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/"
# SHAREPOINT_LIST_NAME = "PDF_Details_List"  # Replace with your list name

# # Microsoft 365 credentials (replace with your actual credentials)
# MS365_CLIENT_ID = "ab141f71-62ee-4dfa-acc4-a2031341ec30"
# MS365_CLIENT_SECRET = ".fA8Q~qQ8pqcVapgO42xk7L6pkkgdlishntVkc.W"
# MS365_TENANT_ID = "d6881518-0789-4bd5-bc4f-fd091c3b1889"

# def get_sharepoint_file_content(filename):
#     try:
#         # Authenticate using Microsoft 365 credentials
#         token_url = f"https://login.microsoftonline.com/{MS365_TENANT_ID}/oauth2/token"
#         token_data = {
#             "grant_type": "client_credentials",
#             "client_id": MS365_CLIENT_ID,
#             "client_secret": MS365_CLIENT_SECRET,
#             "resource": "https://graph.microsoft.com",
#         }
#         response = requests.post(token_url, data=token_data)
#         access_token = response.json().get("access_token")

#         # Fetch the file content using Microsoft Graph API
#         file_url = f"{SHAREPOINT_SITE_URL}/_api/web/lists/getbytitle('{SHAREPOINT_LIST_NAME}')/items?$filter=FileLeafRef eq '{filename}'"
#         headers = {"Authorization": f"Bearer {access_token}"}
#         file_response = requests.get(file_url, headers=headers)
#         file_items = file_response.json().get("value")

#         if file_items:
#             # Check if the file exists in SharePoint
#             file_item = file_items[0]  # Assuming there's only one file with the given name
#             # Retrieve the file content (assuming it's stored in a field named 'FileContent')
#             file_content = file_item.get("Title")
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
