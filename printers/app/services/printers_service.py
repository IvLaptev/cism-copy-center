import json
from typing import List

from app.models.printer import Printer
from app.utils.settings import Settings


settings = Settings()
printers: List[Printer] = json.load(open(f'{settings.path_to_data}'))['printers']

class PrintersService():
    def get_all_printers(self) -> List[Printer]:
        return sorted(printers, key=lambda d: d['printer_name']) 