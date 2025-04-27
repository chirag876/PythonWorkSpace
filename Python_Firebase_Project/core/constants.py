import os
from dotenv import load_dotenv
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)
load_dotenv()

# Firebase
FIREBASE_ADMIN_SDK_PATH = os.getenv("FIREBASE_ADMIN_SDK_PATH")
REALTIME_DATABASE_URL = os.getenv("REALTIME_DATABASE_URL")

# Standard Status Messages
STATUS_CODE_500_MSG = os.getenv("STATUS_CODE_500_MSG", "Internal Server Error")
STATUS_CODE_400_MSG = os.getenv("STATUS_CODE_400_MSG", "Bad Request")
STATUS_CODE_401_MSG = os.getenv("STATUS_CODE_401_MSG", "Unauthorized")
STATUS_CODE_403_MSG = os.getenv("STATUS_CODE_403_MSG", "Forbidden")
STATUS_CODE_404_MSG = os.getenv("STATUS_CODE_404_MSG", "Not Found")

# Custom Messages
USER_NOT_FOUND_MSG = os.getenv("USER_NOT_FOUND_MSG", "User not found")
DATABASE_ERROR_MSG = os.getenv("DATABASE_ERROR_MSG", "Database error occurred")
AUTHENTICATION_ERROR_MSG = os.getenv("AUTHENTICATION_ERROR_MSG", "Authentication failed")
RESOURCE_NOT_FOUND_MSG = os.getenv("RESOURCE_NOT_FOUND_MSG", "The requested resource could not be found")

# Logging
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")

# Retry Config
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5))

# HTTP Status Code Constants
BAD_REQUEST = HTTP_400_BAD_REQUEST
UNAUTHORIZED = HTTP_401_UNAUTHORIZED
FORBIDDEN = HTTP_403_FORBIDDEN
NOT_FOUND = HTTP_404_NOT_FOUND
INTERNAL_ERROR = HTTP_500_INTERNAL_SERVER_ERROR