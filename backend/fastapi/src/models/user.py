from sqlmodel import SQLModel, Field, Column
from typing import Optional
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import text, DateTime

class User(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    contact_type: str = Field(index=True, min_length=5, max_length=5)
    email: Optional[str] = Field(index=True)
    phone: Optional[str] = Field(index=True)
    profile_picture: Optional[str]
    profile_banner: Optional[str]
    password: str
    created: datetime = Field(
      default_factory=datetime.utcnow, 
      sa_column=Column(
        DateTime(timezone=True), 
        nullable=False, 
        server_default=text("CURRENT_TIMESTAMP")
    ))
  