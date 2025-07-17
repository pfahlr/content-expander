# backend/router.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import  HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

#from src.schemas.payloads.registration import RegistrationRequest
#from src.models import AccountStub

router = APIRouter()

@router.get("/proof")
def proofoflife():
  try:
    with open("src/docs/index.html", "r") as file:
      content = file.read()
      file.close()
      return HTMLResponse(content=content)
  except Exception as e: 
    raise HTTPException(500, str(e))
