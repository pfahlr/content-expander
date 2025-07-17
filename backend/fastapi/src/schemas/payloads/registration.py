import re
from typing import Optional, Literal
from sqlmodel import SQLModel, Field
from pydantic import validator

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
PHONE_REGEX = re.compile(r"^\+?\d{10,15}$")
AUTH_REGEX = re.compile(r"^#?([0-9a-fA-F]{6})$")

class RegistrationRequest(SQLModel):
  contact: str = Field(..., description="Email or phone number")
  contact_type: Optional[Literal["email", "phone"]] = None

  @validator("contact")
  def validate_contact(cls, value):
    if EMAIL_REGEX.fullmatch(value):
      return value
    elif PHONE_REGEX.fullmatch(value):
      return value
    raise ValueError("Must be a valid email or phone number")

  @validator("contact_type", always=True)
  def determine_type(cls, v, values):
    contact = values.get("contact")
    if EMAIL_REGEX.fullmatch(contact):
      return "email"
    elif PHONE_REGEX.fullmatch(contact):
      return "phone"
    raise ValueError("Could not determine contact type")

class VerifyRequest(SQLModel):
  auth_code: str = Field(min_length=6, max_length=6)

  @validator("auth_code")
  def validate_auth_code(cls, value):
    if AUTH_REGEX.fullmatch(value) and length(value) == 6:
      log.info("auth code is correct format:"+value)
      return value
    raise ValueError("Must be 6 digit auth code")
