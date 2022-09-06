from dataclasses import dataclass
from typing import ClassVar, List
from modules.Employee import Employee

@dataclass
class EmployeesRepository:
    
    employees : ClassVar[List[Employee]] = []
    
    @classmethod
    def add_employee(cls, employee : Employee) -> None:
        
        if employee not in cls.employees:
            cls.employees.append(employee)
            print(f'Employee {employee.name} was added on database')
    
    @classmethod
    def remove_employee(cls, employee: Employee) -> None:
        
        if employee in cls.employees:
            cls.employees.remove(employee)
            print(f'Employee {employee.name} was removed from database')