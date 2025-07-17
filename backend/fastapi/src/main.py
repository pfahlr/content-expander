# backend/main.py
import os
from dotenv import load_dotenv
from pathlib import Path
# parents[0] is ./, 1 is ../, 2: ../../ , 3: ../../../ 
# we're in [root]/backend/fastapi/src, so need [3] to get back to [root] 
#load_dotenv(dotenv_path=Path(__file__).resolve().parents[3] / ".env")
#print("IN MAIN.PY")
#DATABASE_URL = os.getenv("DATABASE_URL")

from utils.logging import log

from globals import *

from fastapi import FastAPI

from middleware.log_requests import LogRequestMiddleware
from fastapi.middleware.cors import CORSMiddleware
from router import router as api_router
from api.v1 import router as v1_router


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
