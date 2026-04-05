from datetime import datetime

#VALIDAR TEXTO
 
def validate_text(value: str, field_name: str):
    if not isinstance(value, str) or not value.strip():
        return False, f"{field_name} No puede ser vacio."
    
    return True, value.strip()

# VALIDAR SSN

def validate_ssn(ssn: str):
    if not isinstance(ssn, str) or not ssn.strip():
        return False, "SSN No puede ser vacio."

    if not ssn.isdigit():
        return False, "SSN Solo puede contener numeros."
    
    return True, ssn


# VALIDAR SALARIO
def validate_salary(value):
    try:
        salary = float(value)
        if salary <= 0:
            return False, "Salary must be greater than 0."
        return True, salary
    except:
        return False, "Invalid salary format."


# VALIDAR FECHA
def validate_date(date_str: str):
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return True, parsed_date
    except:
        return False, "Invalid date format. Use YYYY-MM-DD."


# VALIDAR ROLE
def validate_role(role: str):
    valid_roles = {"manager", "engineer", "sales", "sales_engineer"}

    role_clean = role.strip().lower()

    if role_clean not in valid_roles:
        return False, f"Invalid role. Valid roles: {', '.join(valid_roles)}"

    return True, role_clean


# VALIDAR DEPARTAMENTO EXISTE
def validate_department_exists(dept_name: str, departments: dict):
    if dept_name not in departments:
        return False, "Department does not exist."
    return True, dept_name


# VALIDAR EMPLEADO EXISTE
def validate_employee_exists(ssn: str, employees: dict):
    if ssn not in employees:
        return False, "Employee does not exist."
    return True, ssn


# VALIDAR PROYECTO EXISTE
def validate_project_exists(name: str, projects: dict):
    if name not in projects:
        return False, "Project does not exist."
    return True, name