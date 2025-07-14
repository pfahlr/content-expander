from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import text, DateTime

#from .content_revision import ContentRevision
from .join_tables import ContentJoinTag
#from .tag import Tag

class Content(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  title: str = Field(default="[empty]", index=True)
  created: datetime = Field(
    default_factory=datetime.utcnow, 
    sa_column=Column(
      DateTime(timezone=True), 
      nullable=False, 
      server_default=text("CURRENT_TIMESTAMP")
    ))
  modified: datetime = Field(default_factory=datetime.utcnow, 
    sa_column=Column(
      DateTime(timezone=True), 
      nullable=False, 
      server_default=text("CURRENT_TIMESTAMP")
    ))

  revisions: List["ContentRevision"] = Relationship(back_populates="content")
  tags: List["Tag"] = Relationship(back_populates="contents", link_model=ContentJoinTag)
