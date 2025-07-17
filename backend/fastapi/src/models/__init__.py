from .user import User
#from .account_stub import AccountStub
from .content import Content
from .content_revision import ContentRevision
from .tag import Tag
from .join_tables import ContentJoinTag

from sqlmodel import SQLModel
from database import engine

def init_db():
    SQLModel.metadata.create_all(engine)