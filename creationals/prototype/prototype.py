from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Worker:
    
    name: str
    register_date: datetime
    hour_salary: float
    working_days: int
    role: Role
    month_bonus: float
    
    @property
    def payment(self) -> float:
        return self.hour_salary * 8 * self.working_days + self.month_bonus 
    
    def clone(self) -> Worker:
        return deepcopy(self)
    
    def __str__(self) -> str:
        return f'{self.name} is a {self.role}, he/she worked {self.working_days} days and will earn {self.payment} this month'


@dataclass 
class Role:
    name : str
    
    def __str__(self) -> str:
        return self.name
    

if __name__ == '__main__':
    
    adm = Role('Administrative Assistant')
    assistant = Worker('worker', register_date=datetime.now(), hour_salary=7, working_days=21, role=adm, month_bonus=400)
    
    john = assistant.clone()
    john.name = 'John'
    
    mary = assistant.clone()
    mary.name = 'Mary'
    
    print(john)
    print(mary)
    