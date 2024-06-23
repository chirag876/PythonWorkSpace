# # from flask import Flask, request, send_file
# # import requests

# # app = Flask(__name__)

# # # SharePoint API Endpoint
# # SHAREPOINT_URL = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/_api/web/lists/getbytitle('PDF_Details_List')/items"

# # # Function to authenticate with SharePoint
# # def authenticate_with_sharepoint():
# #     # Implement authentication logic here
# #     pass

# # # Route to download file
# # @app.route('/download-file', methods=['GET'])
# # def download_file():
# #     # Authenticate with SharePoint
# #     authenticate_with_sharepoint()

# #     # Get file name from request
# #     file_name = request.args.get('file_name')

# #     # Query SharePoint to retrieve file information
# #     response = requests.get(SHAREPOINT_URL, params={"$filter": f"FileLeafRef eq '{file_name}'"})
    
# #     try:
# #         response.raise_for_status()  # Raise exception for 4XX and 5XX status codes
        
# #         # Extract file URL from response
# #         file_url = response.json()["d"]["results"][0]["FileRef"]
        
# #         # Download the file
# #         file_response = requests.get(file_url)
        
# #         # Return file content as response
# #         return send_file(file_response.content, as_attachment=True)
    
# #     except requests.HTTPError as e:
# #         error_message = f"HTTP Error: {e}"
# #         print(error_message)
# #         return error_message
    
# #     except Exception as e:
# #         error_message = f"Error: {e}"
# #         print(error_message)
# #         return error_message

# # if __name__ == '__main__':
# #     app.run(debug=True, port=8000)

# from shareplum import Site
# from shareplum.site import Version
# from flask import Flask, send_file

# app = Flask(__name__)

# # Define the directory where your SharePoint files are stored
# SHAREPOINT_FOLDER = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/_api/web/lists/getbytitle('PDF_Details_List')/items"
# app.config['SHAREPOINT_FOLDER'] = SHAREPOINT_FOLDER

# # SharePoint configuration (replace with your actual details)
# # SHAREPOINT_URL = "https://spectraltechllc.sharepoint.com/sites/AzurePowerApps/Lists/PDF_Details_List/AllItems.aspx"
# SHAREPOINT_USERNAME = "devops@spectraltechllc.onmicrosoft.com"
# SHAREPOINT_PASSWORD = "NTY4UH89H^g%Qm"
# SHAREPOINT_LIST_NAME = "PDF_Details_List"  # Replace with your list name

# def get_sharepoint_file_content(filename):
#     try:
#         # Connect to SharePoint site
#         site = Site(SHAREPOINT_FOLDER, version=Version.v2016, auth=(SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD))

#         # Get the file item by filename
#         file_item = site.List(SHAREPOINT_LIST_NAME).GetItemByFilter({"FileLeafRef": filename})
#         if file_item:
#             # Retrieve the file content (assuming it's stored in a field named 'FileContent')
#             file_content = file_item["FileContent"]
#             return file_content
#         else:
#             print(f"File '{filename}' not found in SharePoint.")
#             return None
#     except Exception as e:
#         print(f"Error retrieving file from SharePoint: {e}")
#         return None

# @app.route("/download/<filename>")
# def download_sharepoint_file(filename):
#     # Get the file content from SharePoint (replace with your actual logic)
#     file_content = get_sharepoint_file_content(filename)

#     if file_content:
#         # Serve the file for download
#         return send_file(
#             file_content,
#             as_attachment=True,
#             attachment_filename=filename,
#             mimetype="application/octet-stream",  # Set the appropriate MIME type
#         )
#     else:
#         return f"File '{filename}' not found in SharePoint."

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)
