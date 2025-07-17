from fastapi_users_db_sqlmodel import SQLModelBaseUserDB, SQLModelUserDatabaseAsync

class User(SQLModelBaseUserDB, table=True):
  pass
  

