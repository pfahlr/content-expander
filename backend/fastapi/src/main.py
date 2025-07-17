# backend/main.py
import os
from dotenv import load_dotenv
from pathlib import Path

#from utils.logging import log

from globals import log

from fastapi import Depends, FastAPI

from middleware.log_requests import LogRequestMiddleware
from fastapi.middleware.cors import CORSMiddleware
from router import router as api_router
from api.v1 import router as v1_router

from models import User 
from database import create_db_and_tables
from src.schemas.payloads.user import UserCreate, UserRead, UserUpdate
from users import auth_backend, current_active_user, fastapi_users

app = FastAPI(
    title="Repaste API",
    description="Convert blog posts into Twitter threads, YouTube scripts, and more.",
    version="0.1.0"
)

# Allow frontend to call the API (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173","*"],  # Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(api_router, prefix="/api")
app.include_router(v1_router, prefix="/api/v1")


# FastAPI USERS 
app.include_router(
  fastapi_users.get_auth_router(auth_backend), 
  prefix="/auth/jwt", 
  tags=["auth"],
)
app.include_router(
  fastapi_users.get_register_router(UserRead, UserCreate),
  prefix="/auth",
  tags=["auth"],
)
app.include_router(
  fastapi_users.get_reset_password_router(),
  prefix="/auth",
  tags=["auth"],
)
app.include_router(
  fastapi_users.get_verify_router(UserRead),
  prefix="/auth",
  tags=["auth"],
)
app.include_router(
  fastapi_users.get_users_router(UserRead, UserUpdate),
  prefix="/users",
  tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}