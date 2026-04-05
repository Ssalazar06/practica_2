from EmployeeService import get_employee_by_ssn
from models.Child import Child
from utils.Validators import *

def add_child_to_employee(employee_ssn: str, child_data: dict, employees: dict):


    ok, employee_ssn = validate_employee_exists(employee_ssn, employees)
    if not ok:
        return False, employee_ssn

    
    ok, name = validate_text(child_data.get("name"), "Child name")
    if not ok:
        return False, name

    ok, birth_date = validate_date(child_data.get("birth_date"))
    if not ok:
        return False, birth_date

    child = Child(name, birth_date, employee_ssn)

    return employees[employee_ssn].add_child(child)

def get_children_by_employee(employee_ssn: str, employees: dict):
    emp = employees.get(employee_ssn)
    if not emp:
        return False, "Emepleado no encontrado."
    return True, emp.get_children()


