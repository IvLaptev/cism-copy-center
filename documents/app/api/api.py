from fastapi import APIRouter

from .endpoints.documents_router import router as documents_router


router = APIRouter()
router.include_router(documents_router, prefix='/documents', tags=['documents'])
