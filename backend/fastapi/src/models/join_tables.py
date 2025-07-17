from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# --- Join Table: Tag <-> Content ---
class ContentJoinTag(SQLModel, table=True):
  __tablename__ = "contentjointag"
  __table_args__ = {"extend_existing": True}
  tag_id: int = Field(foreign_key="tag.id", primary_key=True)
  content_id: int = Field(foreign_key="content.id", primary_key=True)
