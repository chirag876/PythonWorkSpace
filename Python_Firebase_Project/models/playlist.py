from pydantic import BaseModel, Field
from typing import Optional, List

class PlaylistItem(BaseModel):
    # Title is required, should be a non-empty string between 1 and 100 characters.
    title: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)

    # Description is optional, should be a string if provided with a max length of 255 characters.
    description: Optional[str] = Field(None, max_length=255, strip_whitespace=True)

    # Songs is a list of strings, and must contain at least one song.
    songs: List[str] = Field(..., min_items=1)

    # Created by is required, should be a non-empty string between 1 and 100 characters.
    created_by: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
