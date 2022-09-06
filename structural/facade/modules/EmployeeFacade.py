from dataclasses import dataclass
from datetime import datetime
from modules.Employee import Employee
from modules.FileStorage import FileStorage
from modules.EmployeesRepository import EmployeesRepository

@dataclass
class EmployeeFacade:
    
    @staticmethod
    def register_employee(employee: Employee):
        
        url = FileStorage.add_file(employee.name)
        employee.phot_url = url
        
        EmployeesRepository.add_employee(employee)
    
    @staticmethod
    def resignate_employee(employee: Employee):
    
        employee.is_active = False
        employee.phot_url = None
        employee.resignation_date = datetime.now()
        
        FileStorage.delete_file(employee.phot_url)
        EmployeesRepository.remove_employee(employee)
    
