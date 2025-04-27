from firebase_admin import credentials, initialize_app, get_app
from core import logger
from core.constants import FIREBASE_ADMIN_SDK_PATH, REALTIME_DATABASE_URL, STATUS_CODE_500_MSG

def initialize_firebase():
    try:
        get_app()
        logger.info_log("Firebase already initialized.")
    except ValueError:
        if not FIREBASE_ADMIN_SDK_PATH:
            logger.error_log("Missing FIREBASE_ADMIN_SDK_PATH in environment.")
            raise RuntimeError(STATUS_CODE_500_MSG)

        if not REALTIME_DATABASE_URL:
            logger.error_log("Missing REALTIME_DATABASE_URL in environment.")
            raise RuntimeError(STATUS_CODE_500_MSG)

        try:
            cred = credentials.Certificate(FIREBASE_ADMIN_SDK_PATH)
            initialize_app(cred, {"databaseURL": REALTIME_DATABASE_URL})
            logger.info_log("Firebase has been initialized successfully.")
        except Exception as e:
            logger.error_log(f"Failed to initialize Firebase: {str(e)}")
            raise RuntimeError(STATUS_CODE_500_MSG)
