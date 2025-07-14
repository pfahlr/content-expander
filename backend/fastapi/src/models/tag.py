from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

from .join_tables import ContentJoinTag

from .content import Content

class Tag(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: Optional[str] = Field(default=None, unique=True)

  contents: List[Content] = Relationship(back_populates="tags", link_model=ContentJoinTag)


