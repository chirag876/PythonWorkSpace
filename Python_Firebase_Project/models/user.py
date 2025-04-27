from pydantic import BaseModel, EmailStr, Field

from typing import Optional

# ------------ Request Models -------------------

class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=10)
    display_name: Optional[str] = None
    

class UpdateUserRequest(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = Field(default=None, min_length=10)
    display_name: Optional[str] = None
    

# ---------- Response Models ------------------------

class UserResponse(BaseModel):
    uid: str
    email: Optional[str]
    display_name: Optional[str]