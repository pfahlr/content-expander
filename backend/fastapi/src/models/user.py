from fastapi_users_db_sqlmodel import SQLModelBaseUserDB, SQLModelUserDatabaseAsync
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModelBaseUserDB, table=True):
  phone: Optional[str] = Field(unique=True, index=True)
  profile_image: Optional[str] = Field()
  profile_banner: Optional[str] = Field()
  profile_headline: Optional[str] = Field()
  profile_displayname: Optional[str] = Field()


