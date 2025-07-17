# /src/api/v1/registration.py
from utils.logging import log
from globals import *
from fastapi import APIRouter
from fastapi.responses import  HTMLResponse, JSONResponse
from sqlmodel import Session

from src.schemas.payloads.registration import RegistrationRequest, VerifyRequest
from models import AccountStub
from src.services.messaging import MessageDispatcher
from database import engine, get_session
from sqlmodel import Session
router = APIRouter()

@router.get("/")
def index():
  endpoints ='''
  /api/v1/registration | GET<br/>
  /api/v1/registration/register | POST <br/>
  /api/v1/registration/verify | POST <br/>
  '''
  return HTMLResponse(content="/api/v1/registration")

@router.post("/register")
def register_user(registration_req: RegistrationRequest):
  try:
    log.info('register_user endpoint:')
    log.info(registration_req)
    stub = AccountStub(
    contact=registration_req.contact,
    contact_type=registration_req.contact_type
    )
    log.info("stub object assembled")
    log.info(stub)
  except Exception as e:
    log.error("there was an error")
    return {"message":"there was a problem READING your request","error":"01"}
  
  with Session(engine) as session:
    try:
      log.error("commiting account stub")
      session.add(stub)
      session.flush()
      session.refresh(stub)
      log.info('account stub committed, reloading stub object')
      log.info(stub)
    except Exception as e:
      log.error(e)
      log.error("rolling back stub creation")
      session.rollback()
      return {"message":"there was a problem PROCESSING your request", "error":"02"}

    try:
      message_dispatcher = MessageDispatcher()
      subject="Thanks for Registering with "+WEBSITE_NAME+" Please Validate your account!"
      body="Your "+WEBSITE_NAME+" verification code is:\n\n"+stub.auth_code
      message_dispatcher.send_message(stub.contact, stub.contact_type, subject, body, body)
    except Exception as e:
      log.error(e)
      log.error("rolling back stub creation")
      return {"message":"there was a problem SENDING your code", "error":"03"}

    try: 
      response = JSONResponse(content={"message":"verification code sent", "contact": stub.contact, "error":"00"})
      response.set_cookie(
        key="stub_id",
        value=str(stub.id),
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=900  # 15 minutes, match auth_code expiration
        )
      session.commit()
      return response
    except Exception as e:
      log.error(e)
      log.error("rolling back stub creation")
      session.rollback()
      return {"message":"there was a problem CREATING your session", "error":"03"}

@router.post("/verify")
def register_verify(verify_request: VerifyRequest, stub_id: str = Cookie(...), db: Session = Depends(get_db)):
  log.info(db):
  stub = db.get(AccountStub, stub_id)
  log.info(stub)
  if stub.auth_code == verify_request.auth_code: 
    return {"message":"code match"}

