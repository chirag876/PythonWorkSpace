# v1/admin_auth_api.py

from fastapi import APIRouter, HTTPException, Header
from core.firebase import auth
from core import logger
from core.constants import (
    STATUS_CODE_400_MSG,
    STATUS_CODE_401_MSG,
    STATUS_CODE_404_MSG,
    DATABASE_ERROR_MSG,
    AUTHENTICATION_ERROR_MSG,
    USER_NOT_FOUND_MSG
)
from models.user import CreateUserRequest, UpdateUserRequest, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


# Dependency to get the UID from headers
def get_current_user(uid: str = Header(...)):
    """Get the current user based on the UID passed in headers"""
    try:
        user = auth.check_user_exists(uid)
        logger.info_log(f"Authenticated user from header UID: {uid}")
        return user
    except HTTPException as e:
        logger.warning_log(f"Header UID validation failed: {uid}")
        raise e


@router.post("/create", response_model=UserResponse)
def create_user(user: CreateUserRequest):
    try:
        user_record = auth.create_user(**user.model_dump())
        logger.info_log(f"User created: {user_record.uid}")
        return UserResponse(
            uid=user_record.uid,
            email=user_record.email,
            display_name=user_record.display_name
        )
    except Exception as e:
        logger.error_log(f"User creation failed: {str(e)}")
        raise HTTPException(status_code=STATUS_CODE_400_MSG, detail=DATABASE_ERROR_MSG)


@router.get("/{uid}", response_model=UserResponse)
def get_user(uid: str):
    try:
        user_record = auth.get_user_by_uid(uid)
        logger.info_log(f"User fetched: {uid}")
        return UserResponse(
            uid=user_record.uid,
            email=user_record.email,
            display_name=user_record.display_name
        )
    except Exception as e:
        logger.warning_log(f"User not found: {uid} — {str(e)}")
        raise HTTPException(status_code=STATUS_CODE_404_MSG, detail=USER_NOT_FOUND_MSG)


@router.put("/{uid}", response_model=UserResponse)
def update_user(uid: str, user: UpdateUserRequest):
    try:
        user_record = auth.update_user(uid, **user.model_dump(exclude_none=True))
        logger.info_log(f"User updated: {uid}")
        return UserResponse(
            uid=user_record.uid,
            email=user_record.email,
            display_name=user_record.display_name
        )
    except Exception as e:
        logger.error_log(f"User update failed for {uid}: {str(e)}")
        raise HTTPException(status_code=STATUS_CODE_400_MSG, detail=DATABASE_ERROR_MSG)


@router.delete("/{uid}")
def delete_user(uid: str):
    try:
        auth.delete_user(uid)
        logger.info_log(f"User deleted: {uid}")
        return {"message": f"User {uid} deleted successfully."}
    except Exception as e:
        logger.error_log(f"User deletion failed for {uid}: {str(e)}")
        raise HTTPException(status_code=STATUS_CODE_400_MSG, detail=DATABASE_ERROR_MSG)


@router.post("/verify-token")
def verify_token(id_token: str):
    try:
        decoded = auth.verify_id_token(id_token)
        logger.info_log(f"Token verified for UID: {decoded['uid']}")
        return {"uid": decoded["uid"], "claims": decoded}
    except Exception as e:
        logger.warning_log(f"Token verification failed: {str(e)}")
        raise HTTPException(status_code=STATUS_CODE_401_MSG, detail=AUTHENTICATION_ERROR_MSG)
