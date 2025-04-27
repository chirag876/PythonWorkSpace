# v1/playlist_apis.py

from fastapi import APIRouter, HTTPException, Header, Depends
from models.playlist import PlaylistItem
from core.firebase.realtime_playlist import (
    create_playlist,
    get_playlist_by_id,
    get_all_playlists,
    update_playlist,
    delete_playlist,
)
from core.firebase import auth
from core import logger
from core.constants import (
    INTERNAL_ERROR,
    NOT_FOUND,
    DATABASE_ERROR_MSG,
    RESOURCE_NOT_FOUND_MSG,
)

router = APIRouter(prefix="/playlist", tags=["Realtime playlist"])

# Dependency: Check UID from headers
def get_current_user(uid: str = Header(...)):
    """Verify the user by UID (passed in headers)"""
    user = auth.check_user_exists(uid)
    return user

@router.post("/realtime/{path}")
async def create_playlist_item(path: str, playlist: PlaylistItem, current_user: str = Depends(get_current_user)):
    try:
        result = create_playlist(path, playlist.dict())
        logger.info_log(f"Created playlist item in path '{path}'")
        return result
    except Exception as e:
        logger.error_log(f"Error creating playlist item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)

@router.get("/realtime/{path}/{item_id}")
async def read_playlist_item(path: str, item_id: str, current_user: str = Depends(get_current_user)):
    try:
        item = get_playlist_by_id(path, item_id)
        if item:
            logger.info_log(f"Fetched playlist item '{item_id}' from '{path}'")
            return item
        logger.warning_log(f"Playlist item '{item_id}' not found in '{path}'")
        raise HTTPException(status_code=NOT_FOUND, detail=RESOURCE_NOT_FOUND_MSG)
    except Exception as e:
        logger.error_log(f"Error reading playlist item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)

@router.get("/realtime/{path}")
async def read_all_playlists(path: str, current_user: str = Depends(get_current_user)):
    try:
        items = get_all_playlists(path)
        logger.info_log(f"Retrieved all playlist items from '{path}'")
        return items
    except Exception as e:
        logger.error_log(f"Error fetching all playlists: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)

@router.put("/realtime/{path}/{item_id}")
async def update_playlist_item(path: str, item_id: str, playlist: PlaylistItem, current_user: str = Depends(get_current_user)):
    try:
        result = update_playlist(path, item_id, playlist.dict())
        logger.info_log(f"Updated playlist item '{item_id}' in '{path}'")
        return result
    except Exception as e:
        logger.error_log(f"Error updating playlist item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)

@router.delete("/realtime/{path}/{item_id}")
async def delete_playlist_item(path: str, item_id: str, current_user: str = Depends(get_current_user)):
    try:
        result = delete_playlist(path, item_id)
        logger.info_log(f"Deleted playlist item '{item_id}' from '{path}'")
        return result
    except Exception as e:
        logger.error_log(f"Error deleting playlist item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)
