# /src/api/v1/registration.py
from fastapi import APIRouter
from src.schemas.payloads.registration import RegistrationRequest

router = APIRouter()

@router.post("/register")
def register_user(registration_req: RegistrationRequest):
  stub = AccountStub(
    contact=registration_req.contact,
   contact_type=registration_req.contact_type
   )
  with Session(engine) as session:
    session.add(stub)
    session.commuit(stub)
    session.refresh(stub)

  return {"status": "received", "contact": payload.contact}

    