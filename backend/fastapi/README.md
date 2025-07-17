# FastAPI Backend

## Technology Used

[FastAPI](https://fastapi.tiangolo.com/)
[https://fastapi-users.github.io](https://fastapi-users.github.io)
  -[FastAPI Users + SQLModel](https://gist.github.com/juftin/91dee06998771f13788880d387d7022d)[1](https://github.com/fastapi-users/fastapi-users-db-sqlmodel)[2](https://stackoverflow.com/questions/70694787/fastapi-fastapi-users-with-database-adapter-for-sqlmodel-users-table-is-not-crea)
  -[JWT](https://jwt.io/introduction)
    - [JWT Security](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#local-storage)
  -[ES256 JWT Signing](https://blog.authlib.org/2023/openssl-ec-keys)
  
[SQLModel](https://sqlmodel.tiangolo.com/)
[Pydantic](https://docs.pydantic.dev/latest/)
[SQLAlchemy](https://www.sqlalchemy.org/)

## Commands

run server
```
./entrypoint.sh
```

build database schema update scripts
```
alembic revision --autogenerate -m "message""
```

run database schema update scripts
```
alembic upgrade head
```

run database schema rollback script
```
alembic downgrade <version>
```

**FROM PROJECT ROOT**

nuke database container entirely
```
make db-container-nuke
```

start database container
```
make db-container-up
```

stop database container
```
make db-container-down
```





