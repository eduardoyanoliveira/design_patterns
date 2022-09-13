from dataclasses import dataclass
from datetime import datetime


@dataclass
class BeastMemento:
    
    __name: str
    __date: datetime
    __state: str
    
    @property
    def get_date(self) -> datetime:
        return self.__date
    
    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def state(self) -> str:
        return self.__state
    