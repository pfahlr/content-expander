import uuid
from globals import log, WEBSITE_NAME, WEBSITE_FRONTEND_URL, FASTAPI_USERS_SECRET, FASTAPI_VERIFCATION_SECRET, FASTAPI_PW_TOKEN_SECRET, FASTAPI_USERS_PUBLIC_KEY, FASTAPI_USERS_PRIVATE_KEY, FASTAPI_KEYPAIR_ALGO
from typing import Optional
from models import User
from database import get_user_db
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from services.messaging import MessageDispatcher

from fastapi_users.authentication import (
  AuthenticationBackend,
  BearerTransport,
  CookieTransport,  
  JWTStrategy,
)

from fastapi_users_db_sqlmodel import SQLModelUserDatabaseAsync


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
  reset_password_token_secret = FASTAPI_PW_TOKEN_SECRET
  verification_token_secret = FASTAPI_VERIFCATION_SECRET
  message_dispatcher = MessageDispatcher()
  require_verification = True

  async def on_after_register(self, user: User, request: Optional[Request] = None):
    log.info(f"User {user.id} has registered.")
    log.info("calling self.request_verify() manually")
    await self.request_verify(user, request)

  async def on_after_forgot_password(
    self, user: User, token: str, request: Optional[Request] = None
  ):
    subject = "Password Reset Requested for account on "+WEBSITE_NAME+"\n\n"
    message = "Here is your password reset token\n\n: "+token+"\n\n"
    message += "Follow this link to reset your password on the website\n\n"+WEBSITE_FRONTEND_URL+"/reset-password?token="+token+"\n\n"
    try: 
      self.message_dispatcher.send_message(contact=user.email, contact_type='email', subject=subject, body_plaintext=message, body_html=message)
      log.info(f"User {user.id} has forgot their password. Reset token: {token}")
    except Exception as e:
      log.error("Error occured when attempting to send password reset email:"+e)

  async def on_after_request_verify(
    self, user: User, token: str, request: Optional[Request] = None
  ):
    subject = "Welcome to "+WEBSITE_NAME+": Verification Required to Activate Account!"
    message = "Thanks for registering at "+WEBSITE_NAME+".\n\nYou'll just need to verify your account using this verification token:\n\n"+token+"\n\n"
    message += "Follow this link to complete verification:\n\n"+WEBSITE_FRONTEND_URL+"/verify-email?token="+token+"\n\n"    
    try: 
      self.message_dispatcher.send_message(contact=user.email, contact_type='email', subject=subject, body_plaintext=message, body_html=message)
      log.info(f"Verification email requested for user {user.id}. Verification token: {token}")
    except Exception as e:
      log.error("Error occured when attempting to send verification email:"+e)

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