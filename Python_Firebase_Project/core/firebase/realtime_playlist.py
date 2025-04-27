# core/firebase/realtime_playlist.py

from firebase_admin import db
from fastapi import HTTPException
from typing import Dict, Optional
from core import logger
from core.constants import (
    DATABASE_ERROR_MSG,
    RESOURCE_NOT_FOUND_MSG
)

def create_playlist(path: str, data: Dict) -> Dict:
    try:
        ref = db.reference(path)
        new_ref = ref.push(data)  # Automatically generates a unique key
        logger.info_log(f"Created playlist under '{path}' with ID: {new_ref.key}")
        return {"id": new_ref.key, **data}
    except Exception as e:
        logger.error_log(f"Failed to create playlist: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def get_playlist_by_id(path: str, item_id: str) -> Optional[Dict]:
    try:
        ref = db.reference(f"{path}/{item_id}")
        item = ref.get()
        if item:
            logger.info_log(f"Fetched playlist by ID: {item_id} from path: {path}")
            return {"id": item_id, **item}
        logger.warning_log(f"Playlist not found: {item_id} at path: {path}")
        raise HTTPException(status_code=404, detail=RESOURCE_NOT_FOUND_MSG)
    except Exception as e:
        logger.error_log(f"Failed to fetch playlist {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def get_all_playlists(path: str) -> Dict:
    try:
        ref = db.reference(path)
        items = ref.get() or {}
        logger.info_log(f"Fetched all playlists under path: '{path}', count: {len(items)}")
        return items
    except Exception as e:
        logger.error_log(f"Failed to fetch all playlists: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def update_playlist(path: str, item_id: str, data: Dict) -> Dict:
    try:
        ref = db.reference(f"{path}/{item_id}")
        ref.update(data)
        logger.info_log(f"Updated playlist {item_id} at path: {path}")
        return {"id": item_id, "updated_data": data}
    except Exception as e:
        logger.error_log(f"Failed to update playlist {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def delete_playlist(path: str, item_id: str) -> Dict:
    try:
        ref = db.reference(f"{path}/{item_id}")
        ref.delete()
        logger.info_log(f"Deleted playlist {item_id} at path: {path}")
        return {"id": item_id, "deleted": True}
    except Exception as e:
        logger.error_log(f"Failed to delete playlist {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)
