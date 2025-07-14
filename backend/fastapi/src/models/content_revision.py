from sqlmodel import SQLModel, Field, Relationship, Column
from typing import Optional, List
from datetime import datetime, timedelta
import sqlalchemy as sa
from sqlalchemy import text, DateTime
from .content import Content

# --- Content Revision ---
class ContentRevision(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  content_id: int = Field(foreign_key="content.id")
  cms_metadata: Optional[dict] = Field(default=None, sa_column=sa.Column(sa.JSON))
  body: Optional[str] = None
  revision_number: int = Field(default=0)
  created: datetime = Field(
    default_factory=datetime.utcnow, 
    sa_column=Column(
      DateTime(timezone=True), 
      nullable=False, 
      server_default=text("CURRENT_TIMESTAMP")
    ))
  content: Content = Relationship(back_populates="revisions")