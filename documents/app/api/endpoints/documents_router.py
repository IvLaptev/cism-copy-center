from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.services.documents_service import DocumentsService
from app.models.document import Document


router = APIRouter()

@router.get('/', response_model=List[Document], description="Returns all documents with pagination")
def get_documents(page: int = 1, amount: int = 10, doc_service: DocumentsService = Depends()):
    if page < 1 or amount < 1:
        raise HTTPException(status_code=400, detail="Fields 'page' and 'amount' can't be less than 1")
    return doc_service.get_all_documents()[amount * (page - 1):amount * page]
