# /src/api/v1/users.py
from utils.logging import log
from globals import *
from fastapi import APIRouter
from fastapi.responses import  HTMLResponse, JSONResponse
from sqlmodel import Session

from src.schemas.payloads.user import UserAccountEditRequest
from models import AccountStub
from src.services.messaging import MessageDispatcher
from database import engine, get_session
from sqlmodel import Session
router = APIRouter()

@router.post('profile_save')
def user_profile_save(UserAccountEditRequest:user_account_fields):
  return {"not implemented"}

