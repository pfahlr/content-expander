import uuid
from globals import log, FASTAPI_USERS_SECRET, FASTAPI_USERS_PUBLIC_KEY, FASTAPI_USERS_PRIVATE_KEY, FASTAPI_KEYPAIR_ALGO
from typing import Optional
from models import User
from database import get_user_db
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin

from fastapi_users.authentication import (
  AuthenticationBackend,
  BearerTransport,
  CookieTransport,  
  JWTStrategy,
)

from fastapi_users_db_sqlmodel import SQLModelUserDatabaseAsync

SECRET = FASTAPI_USERS_PRIVATE_KEY

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
  reset_password_token_secret = SECRET
  verification_token_secret = SECRET

  async def on_after_register(self, user: User, request: Optional[Request] = None):
    print(f"User {user.id} has registered.")

  async def on_after_forgot_password(
    self, user: User, token: str, request: Optional[Request] = None
  ):
    print(f"User {user.id} has forgot their password. Reset token: {token}")

  async def on_after_request_verify(
    self, user: User, token: str, request: Optional[Request] = None
  ):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLModelUserDatabaseAsync = Depends(get_user_db)):
  yield UserManager(user_db)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
#cookie_transport = CookieTransport(cookie_max_age=3600)

def get_jwt_strategy() -> JWTStrategy:
  return JWTStrategy(secret=FASTAPI_USERS_SECRET, lifetime_seconds=3600)


def get_jwt_ske_strategy() -> JWTStrategy:
  return JWTStrategy(secret=FASTAPI_USERS_PRIVATE_KEY, lifetime_seconds=3600, algorithm=FASTAPI_KEYPAIR_ALGO, public_key=FASTAPI_USERS_PUBLIC_KEY)

auth_backend = AuthenticationBackend(
  name="jwt",
  transport=bearer_transport,
  get_strategy=get_jwt_ske_strategy,
)

#  auth_backend_cookie = AuthenticationBackend(
#    name="jwt-cookie",
#    transport=cookie_transport,
#    get_strategy=get_jwt_ske_strategy,
#  )

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)