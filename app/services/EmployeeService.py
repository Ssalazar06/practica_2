from models.Person import Employee, Manager, Engineer, SalesRepresentative, SalesEngineer
from utils.Validators import *


def register_employee(data: dict, employees: dict, departments: dict):
    ok, ssn = validate_ssn(data.get("ssn"))
    if not ok:
        return False, ssn
    
    if ssn in employees:
        return False, "Empleado ya registrado."
    
    ok, role = validate_role(data.get("role"))
    if not ok:
        return False, role
    
    ok, dept_name = validate_department_exists(data.get("department"), departments)
    if not ok:
        return False, dept_name
    
    dept = departments.get(data["department"])
    if not dept:
        return False, "Departamento no encontrado."
    
    ok, first_name = validate_text(data.get("first_name"), "First name")
    if not ok:
        return False, first_name
    
    ok, middle_name = validate_text(data.get("middle_name"), "Middle name")
    if not ok:
        return False, middle_name
    
    ok, last_name = validate_text(data.get("last_name"), "Last name")
    if not ok:
        return False, last_name
    
    ok, second_last_name = validate_text(data.get("second_last_name"), "Second last name")
    if not ok:
        return False, second_last_name
    
    ok, salary = validate_salary(data.get("salary"))
    if not ok:
        return False, salary
    
    ok, birth_date = validate_date(data.get("birth_date"))
    if not ok:
        return False, birth_date
    
    role = data["role"].lower()

    try:
        if role == "manager":
            emp = Manager(**data)
        elif role == "engineer":
            emp = Engineer(**data)
        elif role == "sales":
            emp = SalesRepresentative(**data)
        elif role == "salesEngineer":
            emp = SalesEngineer(**data)
    except Exception as e:
        return False, str(e)
    
    employees[ssn] = emp
    dept.add_employee_ssn(ssn)

    return True, "Empleado registrado exitosamente."

def get_employee_by_department(dept_name: str, departments: dict, employees: dict):
    dept = departments.get(dept_name)
    if not dept:
        return False, "Departamento no encontrado."

    result = []

    for ssn in dept.get_employee_ssns(): #Crear metodo en department
        emp = employees.get(ssn)
        if emp:
            result.append(emp) 

    return True, result

def get_employee_by_ssn(ssn: str, employees: dict):
    emp = employees.get(ssn)
    if not emp:
        return False, "Empleado no encontrado."
    
    return True, emp