from globals import DATABASE_URL, ASYNC_DATABASE_URL, log

from sqlmodel import create_engine, Session

#for fastapi-users
from collections.abc import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from fastapi_users_db_sqlmodel import SQLModelBaseUserDB, SQLModelUserDatabaseAsync
from models import User

# Create the sqlmodel engine
log.info('opening sqlmodel database connection')
engine = create_engine(DATABASE_URL, echo=True)
log.info(engine)

# sqlmodel session getter
def get_session():
  with Session(engine) as session:
    yield session

# create the async engine for fastapi-users
log.info('opening asyncio database connection (for fastapi-user)')
async_engine = create_async_engine(ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
log.info('async_engine:')
log.info(async_engine)
log.info('async_session_maker:')
log.info(async_session_maker)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  async with async_session_maker() as async_session:
    log.info('get_async_session()')
    yield async_session

async def create_db_and_tables():
  async with async_engine.begin() as conn:
    log.info('create_db_and_tables()')
    await conn.run_sync(SQLModel.metadata.create_all)

async def get_user_db(async_session: AsyncSession = Depends(get_async_session)):
  log.info('get_user_db()')
  yield SQLModelUserDatabaseAsync(async_session, User)

