from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Printer(BaseModel):
    printer_uuid: UUID
    printer_name: str
    printer_type: datetime
    printer_address: datetime
