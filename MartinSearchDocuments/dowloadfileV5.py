from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

# SharePoint site URL
site_url = "https://abc.sharepoint.com/sites/AzurePowerApps/"

# Username and password
username = "abc.onmicrosoft.com"
password = "chirdf^g%Qm"

# Authenticate
ctx_auth = AuthenticationContext(site_url)
ctx_auth.acquire_token_for_user(username, password)
ctx = ClientContext(site_url, ctx_auth)

# Specify the document library name and file name
library_name = "Sample_PDF"
file_name = "20240207105157.pdf"  # Replace with the actual file

# Get the file object
file_to_download = File.open_binary(ctx, f"/{library_name}/{file_name}")

# Download location on your machine
download_path = f"./downloads/{file_name}"

# Download the file content
with open(download_path, "wb") as local_file:
    local_file.write(file_to_download.content)

print(f"Downloaded {file_name} to {download_path}")
