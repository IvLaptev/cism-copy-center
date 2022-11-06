from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.services.printers_service import PrintersService
from app.models.printer import Printer


router = APIRouter()

@router.get('/', response_model=List[Printer], description="Returns all printers with pagination")
def get_printers(page: int = 1, amount: int = 10, printer_service: PrintersService = Depends()):
    if page < 1 or amount < 1:
        raise HTTPException(status_code=400, detail="Fields 'page' and 'amount' can't be less than 1")
    return printer_service.get_all_printers()[amount * (page - 1):amount * page]
