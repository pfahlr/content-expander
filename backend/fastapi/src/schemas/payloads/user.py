import uuid
from fastapi_users import schemas
from typing import Optional
from sqlmodel import SQLModel

class UserRead(schemas.BaseUser[uuid.UUID]):
    phone: Optional[str] = None
    profile_image: Optional[str] = None
    profile_banner: Optional[str] = None
    profile_headline: Optional[str] = None
    profile_displayname: Optional[str] = None

class UserCreate(schemas.BaseUserCreate):
    phone: Optional[str] = None
    profile_image: Optional[str] = None
    profile_banner: Optional[str] = None
    profile_headline: Optional[str] = None
    profile_displayname: Optional[str] = None

class UserUpdate(schemas.BaseUserUpdate):
    phone: Optional[str]  = None
    profile_image: Optional[str] = None
    profile_banner: Optional[str] = None
    profile_headline: Optional[str] = None
    profile_displayname: Optional[str] = None
