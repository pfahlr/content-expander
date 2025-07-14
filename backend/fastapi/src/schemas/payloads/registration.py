import re
from typing import Optional, Literal
from sqlmodel import SQLModel, Field
from pydantic import validator

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
PHONE_REGEX = re.compile(r"^\+?\d{10,15}$")

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
