from models.Department import Department
from models.DepartmentLocation import DepartmentLocation
from models.Person import Person, Employee
from utils.Validators import validate_text
def register_department(name:str, departments: dict):
    """Registrar un nuevo departamento si no existe"""
    ok, name = validate_text(name, "Nombre del departamento")
    if not ok:
        return False, name

    if name in departments:
        return False, "Departamento ya existe."

    dept = Department(name)
    departments[name] = dept
    return True, "Departamento registrado."

def add_location_to_department(dept_name:str,address: str, departments: dict) -> tuple[bool, str]:
    """Agregar una nueva ubicación a un departamento que exista"""
    
    ok, dept_name = validate_text(dept_name, "Nombre del departamento")

    if not ok:
        return False, dept_name
    ok, address = validate_text(address, "Direccion")

    if not ok:
        return False, address
    
    dept = departments.get(dept_name)
    if not dept:
        return False, "Departamento no encontrado."
    
    location = DepartmentLocation(address)

    return dept.add_location(location)

def assign_manager(dept_name: str, manager_ssn: str, departments: dict):
    """Asignar un administrador a un departamento"""

    pass