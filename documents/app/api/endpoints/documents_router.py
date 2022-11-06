from typing import List
from fastapi import APIRouter, Depends

from app.services.documents_service import DocumentsService
from app.models.document import Document


router = APIRouter()

@router.get('/', response_model=List[Document], description="Returns all documents with pagination")
def get_documents(doc_server: DocumentsService = Depends()):
    return doc_server.get_all_documents()
