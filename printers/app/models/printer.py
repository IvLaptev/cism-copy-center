from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Printer(BaseModel):
    printer_uuid: UUID
    printer_name: str
    printer_type: str
    printer_address: str
