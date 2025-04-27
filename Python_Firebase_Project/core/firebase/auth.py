from firebase_admin import auth
from fastapi import HTTPException
from core import logger
from core.constants import  STATUS_CODE_500_MSG,  USER_NOT_FOUND_MSG,  AUTHENTICATION_ERROR_MSG


def create_user(email: str, password: str, display_name: str = None):
    """Create a new user with email, password, optional display name"""
    try:
        user = auth.create_user(email=email, password=password, display_name=display_name)
        logger.info_log(f"User created with email: {email}")
        return user
    except Exception as e:
        logger.error_log(f"Error creating user {email}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=STATUS_CODE_500_MSG
        )

def get_user_by_uid(uid: str):
    """Get the user by their UID"""
    try:
        user = auth.get_user(uid)
        logger.info_log(f"User fetched by UID: {uid}")
        return user
    except auth.UserNotFoundError:
        logger.error_log(f"User not found with UID: {uid}")
        raise HTTPException(
            status_code=401,
            detail=USER_NOT_FOUND_MSG
        )
    except Exception as e:
        logger.error_log(f"Error fetching user {uid}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=STATUS_CODE_500_MSG
        )

def update_user(uid: str, **kwargs):
    """Update user by their UID"""
    try:
        user = auth.update_user(uid, **kwargs)
        logger.info_log(f"User updated with UID: {uid}")
        return user
    except Exception as e:
        logger.error_log(f"Error updating user {uid}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=STATUS_CODE_500_MSG
        )

def delete_user(uid: str):
    """Delete user by their UID"""
    try:
        auth.delete_user(uid)
        logger.info_log(f"User deleted with UID: {uid}")
    except Exception as e:
        logger.error_log(f"Error deleting user {uid}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=STATUS_CODE_500_MSG
        )

def verify_id_token(id_token: str):
    """Verify the Firebase ID token to authenticate requests"""
    try:
        decoded_token = auth.verify_id_token(id_token)
        logger.info_log("ID token verified successfully")
        return decoded_token
    except Exception as e:
        logger.error_log(f"Error verifying ID token: {str(e)}")
        raise HTTPException(
            status_code=401,
            detail=AUTHENTICATION_ERROR_MSG
        )

def check_user_exists(uid: str):
    """Check if a user exists by UID"""
    try:
        user = auth.get_user(uid)  # Get the user by UID
        return user  # Return the user if they exist
    except auth.UserNotFoundError:
        logger.error_log(f"User not found with UID: {uid}")
        raise HTTPException(
            status_code=401,
            detail=USER_NOT_FOUND_MSG
        )
    except Exception as e:
        logger.error_log(f"Error checking user existence {uid}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=STATUS_CODE_500_MSG
        )
