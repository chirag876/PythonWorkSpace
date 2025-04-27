# v1/music_apis.py
from fastapi import APIRouter, HTTPException, Header, Depends
from core.firebase.firestore_music import (
    create_music_item,
    get_music_item_by_id,
    get_all_music_items,
    update_music_item,
    delete_music_item
)
from core.firebase import auth
from core import logger
from core.constants import (
    INTERNAL_ERROR,
    NOT_FOUND,
    STATUS_CODE_500_MSG,
    RESOURCE_NOT_FOUND_MSG,
    DATABASE_ERROR_MSG
)
from models.music import MusicItem, UpdateMusicItem

router = APIRouter(prefix="/music", tags=["Firestore Music"])

# 🔐 Dependency: Check user based on UID in headers
def get_current_user(uid: str = Header(...)):
    """Verify the user by UID (passed in headers)"""
    user = auth.check_user_exists(uid)
    return user

@router.post("/{collection_name}")
async def create_music(collection_name: str, music: MusicItem, current_user: str = Depends(get_current_user)):
    """Create a new music item in the specified Firestore collection."""
    try:
        created_music = create_music_item(collection_name, music.dict())
        logger.info_log(f"Created new music item in collection '{collection_name}'")
        return {"item": created_music}
    except Exception as e:
        logger.error_log(f"Error creating music item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)

@router.get("/{collection_name}/{item_id}")
async def read_music(collection_name: str, item_id: str, current_user: str = Depends(get_current_user)):
    """Get a music item by ID from the specified collection."""
    try:
        music = get_music_item_by_id(collection_name, item_id)
        if music:
            logger.info_log(f"Fetched music item with ID '{item_id}' from '{collection_name}'")
            return {"id": item_id, "music_data": music}
        else:
            logger.warning_log(f"Music item not found: {item_id}")
            raise HTTPException(status_code=NOT_FOUND, detail=RESOURCE_NOT_FOUND_MSG)
    except Exception as e:
        logger.error_log(f"Error fetching music item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=STATUS_CODE_500_MSG)

@router.get("/{collection_name}")
async def read_all_music(collection_name: str, current_user: str = Depends(get_current_user)):
    """Get all music items from the specified collection."""
    try:
        music_items = get_all_music_items(collection_name)
        logger.info_log(f"Retrieved all items from collection '{collection_name}'")
        return {"items": music_items}
    except Exception as e:
        logger.error_log(f"Error reading all music items: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=STATUS_CODE_500_MSG)

@router.put("/{collection_name}/{item_id}")
async def update_music(collection_name: str, item_id: str, music: UpdateMusicItem, current_user: str = Depends(get_current_user)):
    """Update a music item partially by ID using merge in Firestore."""
    try:
        updated_music = update_music_item(collection_name, item_id, music.dict(exclude_unset=True))
        logger.info_log(f"Updated music item with ID '{item_id}' in '{collection_name}'")
        return {"id": item_id, "updated_data": updated_music}
    except Exception as e:
        logger.error_log(f"Error updating music item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)


@router.delete("/{collection_name}/{item_id}")
async def delete_music(collection_name: str, item_id: str, current_user: str = Depends(get_current_user)):
    """Delete a music item by ID from the specified collection."""
    try:
        logger.info_log(f"Deleting music item with ID '{item_id}' from '{collection_name}'")
        return delete_music_item(collection_name, item_id)
    except Exception as e:
        logger.error_log(f"Error deleting music item: {str(e)}")
        raise HTTPException(status_code=INTERNAL_ERROR, detail=DATABASE_ERROR_MSG)
