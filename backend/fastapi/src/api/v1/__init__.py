from fastapi import APIRouter
from .users import router as users_router
from .content import router as content_router
from .registration import router as registration_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(content_router, prefix="/content", tags=["content"])
router.include_router(registration_router, prefix="/registration", tags=["registration"])
