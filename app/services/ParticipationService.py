from utils.Validators import *

def assign_employee_to_project(ssn: str, project_name: str, employees: dict, projects: dict):
    ok, ssn = validate_employee_exists(ssn, employees)
    if not ok:
        return False, ssn

    ok, project_name = validate_project_exists(project_name, projects)
    if not ok:
        return False, project_name

    emp = employees[ssn]
    project = projects[project_name]

    if not emp.can_join_projects():
        return False, "Employee role cannot join projects."

    ok, msg = project.add_participant(ssn)
    if not ok:
        return False, msg

    if hasattr(emp, "assign_project"):
        emp.assign_project(project)
    
    return True, "Empleado asignado exitosamente"
