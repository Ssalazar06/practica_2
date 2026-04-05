from models.Project import Project
from utils.Validators import *
def register_project(data: dict, projects: dict, departments: dict):
    ok, name = validate_text(data.get("name"), "Project name")
    if not ok:
        return False, name

    if name in projects: 
        return False, "Proyecto ya registrado."
    
    ok, start_date = validate_date(data.get("start_date"))
    if not ok:
        return False, start_date
    
    ok, dept_name = validate_department_exists(data.get("departament"), departments)
    if not ok:
        return False, dept_name

    project = Project(name, start_date, dept_name)
    departments[dept_name].add_project_name(name) 

    return True, "Proyecto registrado exitosamente."

def get_project_by_department(dept_name:str, departments: dict, projects: dict):
    dept = departments.get(dept_name)
    if not dept:
        return False, "Departamento no encontrado."
    
    result = []
    for name in dept.get_project_names():
        proj = projects.get(name)
        if proj:
            result.append(proj)

        return True, result