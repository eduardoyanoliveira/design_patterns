from datetime import datetime
from typing import Protocol


class IMemento(Protocol):
    
    def get_name(self) -> str: pass
    
    def get_date(self) -> datetime: pass