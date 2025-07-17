from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from datetime import datetime, timedelta
import sqlalchemy as sa
from sqlalchemy import text, DateTime,String
import hashlib
import random 

class AccountStub(SQLModel, table=True):
  __tablename__ = "accountstub"
  __table_args__ = {"extend_existing": True}
  id: Optional[int] = Field(default=None, primary_key=True)
  contact: Optional[str] = Field(index=True)
  contact_type: Optional[str] = Field(index=True)
  auth_code: str = Field(
    default_factory=lambda:hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:6],
    sa_column=Column(
      String(length=6),
      nullable=False,
      server_default=text("substr(md5(random()::text), 1, 6)")
    )
  )
  expires: datetime = Field(
    default_factory=lambda: datetime.utcnow() + timedelta(minutes=15),
    sa_column=Column(
      DateTime(timezone=True), 
      nullable=False, 
      server_default=text("CURRENT_TIMESTAMP + INTERVAL '15 MINUTES'")
  ))

    

