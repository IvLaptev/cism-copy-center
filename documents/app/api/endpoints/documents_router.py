from fastapi import APIRouter, Depends

from app.services.documents_service import DocumentsService


router = APIRouter()

@router.get('/')
def get_documents(doc_server: DocumentsService = Depends()):
    return doc_server.get_all_documents()
