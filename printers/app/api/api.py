from fastapi import APIRouter

from .endpoints.printers_router import router as documents_router


router = APIRouter()
router.include_router(documents_router, prefix='/printers', tags=['printers'])
