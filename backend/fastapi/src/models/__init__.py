from .user import User

from .content import Content
from .content_revision import ContentRevision
from .tag import Tag
from .join_tables import ContentJoinTag

from .subscription import Subscription

from sqlmodel import SQLModel
from database import engine

def init_db():
    SQLModel.metadata.create_all(engine)