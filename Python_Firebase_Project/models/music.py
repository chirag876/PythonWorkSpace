from pydantic import BaseModel, Field, constr, conint
from typing import Optional

# MusicItem represents the schema for creating a new music record.
class MusicItem(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)

    artist: str = Field(..., min_length=1, strip_whitespace=True)

    genre: str = Field(..., max_length=50, strip_whitespace=True)

    year: int = Field(0, ge=1900, le=2100, description="Year must be between 1900 and 2100")


# UpdateMusicItem is for PATCH-like updates. All fields are optional.
class UpdateMusicItem(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, strip_whitespace=True)
    artist: Optional[str] = Field(None, min_length=1, max_length=100, strip_whitespace=True)
    genre: Optional[str] = Field(None, max_length=50, strip_whitespace=True)
    year: Optional[int] = Field(None, ge=1900, le=2100)
