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