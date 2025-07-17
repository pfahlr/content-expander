import re
from typing import Optional, Literal
from sqlmodel import SQLModel, Field
from pydantic import validator

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
PHONE_REGEX = re.compile(r"^\+?\d{10,15}$")
AUTH_REGEX = re.compile(r"^#?([0-9a-fA-F]{6})$")
IMAGE_REGEX = re.compile(r"(?i)\.(jpe?g|png|webp|avif)$")
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])[A-Za-z\d@$!%*?&^#()\-_=+]{8,32}$")

class UserAccountEditRequest(SQLModel):
  email: Optional[str] = Field(index=True)
  phone: Optional[str] = Field(index=True)
  profile_picture: Optional[str] = Field(...)
  profile_banner: Optional[str] = Field(...)
  password: Optional[str] = Field(index=True, min_length=8,max_length=32)


  @validator("password")
  def validate_password(cls,value):
    if value is None: 
      return value
    elif PASSWORD_REGEX.fullmatch(value):
      return value
    raise ValueError("Must be 8 to 32 characters long and include at least 1: uppercase letter, lowercase letter, digit, and special character of @$!%*?&^#()-_=+ ")      


  @validator("profile_picture")
  def validate_banner(cls, value):
    return self.validate_image(value)
  
  @validator("profile_banner")
  def validate_image(cls, value):
    if value is None: 
      return value
    elif IMAGE_REGEX.fullmatch(value):
      return value
    raise ValueError("Must be a valid path to an image file")      

  @validator("email")
  def validate_contact(cls, value):
    if value is None: 
      return value
    elif EMAIL_REGEX.fullmatch(value):
      return value
    raise ValueError("Must be a valid email or phone number")
  
  @validator("phone")
  def validate_contact(cls, value):
    if value is None:
      return value
    elif PHONE_REGEX.fullmatch(value):
      return value
    raise ValueError("Must be a valid email or phone number")

