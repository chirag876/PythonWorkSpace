# core/firebase/firestore_music.py

from firebase_admin import firestore
from fastapi import HTTPException
from typing import Dict
from core import logger
from core.constants import (
    DATABASE_ERROR_MSG,
    RESOURCE_NOT_FOUND_MSG
)

def get_firestore_client():
    try:
        return firestore.client()
    except Exception as e:
        logger.error_log(f"Error initializing Firestore client: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def create_music_item(collection_name: str, data: Dict):
    try:
        db = get_firestore_client()
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(data)
        logger.info_log(f"Music item created in '{collection_name}' with ID: {doc_ref.id}")
        return {"id": doc_ref.id, **data}
    except Exception as e:
        logger.error_log(f"Failed to create music item: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def get_music_item_by_id(collection_name: str, item_id: str):
    try:
        db = get_firestore_client()
        doc = db.collection(collection_name).document(item_id).get()
        if doc.exists:
            logger.info_log(f"Music item fetched by ID: {item_id} from '{collection_name}'")
            return {"id": doc.id, **doc.to_dict()}
        logger.warning_log(f"Music item not found: {item_id} in '{collection_name}'")
        raise HTTPException(status_code=404, detail=RESOURCE_NOT_FOUND_MSG)
    except Exception as e:
        logger.error_log(f"Failed to get music item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def get_all_music_items(collection_name: str):
    try:
        db = get_firestore_client()
        items = db.collection(collection_name).stream()
        data = [{"id": item.id, **item.to_dict()} for item in items]
        logger.info_log(f"Fetched all music items from '{collection_name}', count: {len(data)}")
        return data
    except Exception as e:
        logger.error_log(f"Failed to get all music items: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def update_music_item(collection_name: str, item_id: str, data: Dict):
    try:
        db = get_firestore_client()
        db.collection(collection_name).document(item_id).set(data, merge=True)
        logger.info_log(f"Updated music item {item_id} in '{collection_name}'")
        return {"id": item_id, **data}
    except Exception as e:
        logger.error_log(f"Failed to update music item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)

def delete_music_item(collection_name: str, item_id: str):
    try:
        db = get_firestore_client()
        db.collection(collection_name).document(item_id).delete()
        logger.info_log(f"Deleted music item {item_id} from '{collection_name}'")
        return {"id": item_id, "deleted": True}
    except Exception as e:
        logger.error_log(f"Failed to delete music item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=DATABASE_ERROR_MSG)
