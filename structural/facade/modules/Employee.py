from dataclasses import dataclass
from datetime import datetime as date


@dataclass
class Employee:
    
    name: str
    salary: float
    phot_url: str | None = None
    __is_active: bool = True
    resignation_date: date | None = None
    register_date: date = date.now()
    
    @property
    def is_active(self) -> bool:
        return self.__is_active
    
    @is_active.setter
    def is_active(self, value: bool) -> None:
        self.__is_active = value
    