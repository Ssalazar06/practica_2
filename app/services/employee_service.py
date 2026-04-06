from datetime import date
from typing import Callable

from models.department import Department
from models.person import Employee, Engineer, Manager, SalesEngineer, SalesRepresentative


class EmployeeService:
    """Handle employee registration and queries."""

    def __init__(
        self,
        find_department: Callable[[str], tuple[Department | None, str | None]],
        link_employee_to_department: Callable[[str, str], tuple[bool, str]],
        unlink_employee_from_department: Callable[[str, str], tuple[bool, str]],
        assign_manager_to_department: Callable[[str, str], tuple[bool, str]],
        find_employee_projects: Callable[[str], tuple[list[str] | None, str | None]],
    ):
        """Initialize employee service with department dependency."""
        self.__find_department = find_department
        self.__link_employee_to_department = link_employee_to_department
        self.__unlink_employee_from_department = unlink_employee_from_department
        self.__assign_manager_to_department = assign_manager_to_department
        self.__find_employee_projects = find_employee_projects
        self.__employees: list[Employee] = []
        self.__employees_by_ssn: dict[str, Employee] = {}

    def register_employee(
        self,
        role_name: str,
        ssn: str,
        salary: float,
        department_name: str,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ) -> tuple[Employee | None, str | None]:
        """Register one employee according to role."""
        try:
            normalized_ssn = ssn.strip()
            if normalized_ssn in self.__employees_by_ssn:
                return None, "Ya existe un empleado con ese documento."

            department, error_message = self.__find_department(department_name.strip())
            if department is None:
                return None, error_message if error_message is not None else "No se encontró el departamento."

            role_key = role_name.strip().lower()
            employee_class = self.__resolve_employee_class(role_key)
            if employee_class is None:
                return None, "Rol de empleado no válido."

            employee = employee_class(
                normalized_ssn,
                salary,
                department,
                person_id.strip(),
                first_name.strip(),
                middle_name.strip(),
                last_name.strip(),
                second_last_name.strip(),
                birth_date,
            )
            linked, linked_message = self.__link_employee_to_department(department.get_name(), normalized_ssn)
            if not linked:
                return None, linked_message
            if isinstance(employee, Manager):
                assigned, assigned_message = self.__assign_manager_to_department(department.get_name(), normalized_ssn)
                if not assigned:
                    self.__unlink_employee_from_department(department.get_name(), normalized_ssn)
                    return None, assigned_message
            self.__employees.append(employee)
            self.__employees_by_ssn[normalized_ssn] = employee
            return employee, None
        except Exception as error:
            return None, str(error)

    def get_employee(self, ssn: str) -> tuple[Employee | None, str | None]:
        """Return one employee by SSN."""
        employee = self.__employees_by_ssn.get(ssn.strip())
        return (employee, None) if employee is not None else (None, "No se encontró el empleado.")

    def list_employees(self) -> tuple[list[Employee], str | None]:
        """Return all registered employees."""
        return self.__employees.copy(), None

    def list_employees_by_department(self, department_name: str) -> tuple[list[Employee], str | None]:
        """Return employees of one department."""
        filtered_employees = [
            employee
            for employee in self.__employees
            if employee.get_department().get_name().lower() == department_name.strip().lower()
        ]
        return filtered_employees, None

    def list_employees_by_role(self, role_name: str) -> tuple[list[Employee], str | None]:
        """Return employees filtered by role."""
        role_key = role_name.strip().lower()
        employee_class = self.__resolve_employee_class(role_key)
        if employee_class is None:
            return [], "Rol de empleado no válido."
        filtered_employees = [employee for employee in self.__employees if isinstance(employee, employee_class)]
        return filtered_employees, None

    def get_employee_role_name(self, employee: Employee) -> str:
        """Return one normalized role name from employee instance."""
        if isinstance(employee, Manager):
            return "gerente"
        if isinstance(employee, SalesRepresentative):
            return "representante de ventas"
        if isinstance(employee, SalesEngineer):
            return "ingeniero de ventas"
        return "ingeniero" if isinstance(employee, Engineer) else "empleado"

    def remove_employee(
        self, ssn: str
    ) -> tuple[bool, str]:
        """Remove one employee if employee has no children or projects."""
        try:
            employee, error_message = self.get_employee(ssn)
            if employee is None:
                return False, error_message if error_message is not None else "No se encontró el empleado."
            if employee.get_children():
                return False, "No se puede eliminar un empleado con hijos registrados."
            employee_projects, projects_error = self.__find_employee_projects(ssn)
            if employee_projects is None:
                return False, projects_error if projects_error is not None else "No se pudieron verificar los proyectos del empleado."
            if employee_projects:
                return False, "No se puede eliminar un empleado con proyectos asignados."
            unlinked, unlink_message = self.__unlink_employee_from_department(
                employee.get_department().get_name(), employee.get_ssn()
            )
            if not unlinked:
                return False, unlink_message
            self.__employees.remove(employee)
            self.__employees_by_ssn.pop(employee.get_ssn(), None)
            return True, "Empleado eliminado."
        except Exception as error:
            return False, str(error)

    def __resolve_employee_class(
        self, role_key: str
    ) -> type[Manager] | type[SalesRepresentative] | type[Engineer] | type[SalesEngineer] | None:
        """Resolve role keyword to employee class."""
        role_map: dict[str, type[Manager] | type[SalesRepresentative] | type[Engineer] | type[SalesEngineer]] = {
            "manager": Manager,
            "sales_representative": SalesRepresentative,
            "engineer": Engineer,
            "sales_engineer": SalesEngineer,
        }
        return role_map.get(role_key)
