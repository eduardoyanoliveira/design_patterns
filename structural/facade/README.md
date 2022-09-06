# Facade

### Type: Structural

## Introduction

Analogous to a facade in architecture, a facade is an object that serves as a front-facing interface masking more complex underlying or structural code.Altough the facade pattern is an encapsulation of a complex code, the complex code parts can be used without the Facade Class.

## Advantages

*. Improve the readability and usability of a software library by masking interaction with more complex components behind a single (and often simplified) API.

* Provide a context-specific interface to more generic functionality (complete with context-specific input validation).

## Disadvantages

* Increase the code coheasion, because it's implementation are based on instance and not on interfaces.

* Breaks the open/closed principle

* Breaks the Dependency principle

## Our Python example

### Introduction

The program is meant to be a employee registration system, where a new employee can be registered or resignated at any time. 


#### Employee class

1. The employee class contains: <br>
the employee photo url that need to be provide by a file upload system. <br>
a is_active flag that needs to be False if the employee has been resignated.
a resignated date that will be fufilled at the resignation time.<br>
The other employees attributes are not key factor for the facade example.

```
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
    
```

#### File Storage class

2. The File Storage class provides: <br>
A list of all files urls that are saved on server as a class variable. <br>
A add_file class method that will add a file to the list and return the url generated.<br>
A remove_file class method.<br>

```
from dataclasses import dataclass
from typing import ClassVar, List


@dataclass
class FileStorage:
    
    files: ClassVar[List[str]] = []
    
    @classmethod
    def add_file(cls, file) -> str:
        
        url = f'https://localhost:3000/files/{file}'
        cls.files.append(url)
        
        print(f'File {file} has been uploaded to server')
        return url

    @classmethod
    def delete_file(cls, file) -> None:
        
        if file in cls.files:
            cls.files.remove(file)
            print(f'File {file} has been removed from server')

```

#### Employee Repository

3. This class acts like a database repository that will storage all the employees.It follows the same logic as the File Storage class.

```
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
```

#### The Facade

The Employee Facade encapsulates all the necessary logic to register or resignate a employee and provides to the client code two static methods: resignate_employee and register_employee.

When a new employee is register,he/she must has the photo uploaded to the server and be register on database.At mean while when he/she is resignated, the photo has to be deleted from server, the register removed from database and the resignation_date must be setted

```
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
```

#### The Program

1. Instantiate a employee (yan).
2. Uses the Facade to register the employee.
3. Uses the Facade to resignate the employee.

```
from modules.Employee import Employee
from modules.EmployeeFacade import EmployeeFacade

if __name__ == '__main__':
    emp = Employee(name='Yan', salary=3000)
    print('######')
    print(emp)
    print('######')
    
    print()
    
    EmployeeFacade.register_employee(emp)
    
    print()
    
    
    EmployeeFacade.resignate_employee(emp)
    
    print()
    
    print('######')
    print(emp)
    print('######')

```
