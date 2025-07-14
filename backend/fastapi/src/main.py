# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router as repaste_router

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
app.include_router(repaste_router, prefix="/api")
