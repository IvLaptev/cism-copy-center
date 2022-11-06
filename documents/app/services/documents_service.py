import os
import json
from typing import List

from app.models.document import Document
from app.utils.settings import Settings


settings = Settings()
documents: List[Document] = json.load(open(f'{settings.path_to_data}'))['documents']

class DocumentsService():
    def get_all_documents(self) -> List[Document]:
        return sorted(documents, key=lambda d: d['document_name']) 