from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Document(BaseModel):
    document_uuid: UUID
    document_name: str
    document_created: datetime
    document_edited: datetime
