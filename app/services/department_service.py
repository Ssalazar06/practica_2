from models.department import Department
from models.department_location import DepartmentLocation


class DepartmentService:
    """Handle department business operations."""

    def __init__(self):
        """Initialize in-memory structures for departments."""
        self.__departments: list[Department] = []
        self.__departments_by_name: dict[str, Department] = {}
        self.__managed_department_by_manager_ssn: dict[str, str] = {}

    def register_department(self, department_name: str) -> tuple[bool, str]:
        """Register one department if name is unique."""
        try:
            normalized_name = department_name.strip()
            if normalized_name in self.__departments_by_name:
                return False, "Ya existe un departamento con ese nombre."
            department = Department(normalized_name)
            self.__departments.append(department)
            self.__departments_by_name[normalized_name] = department
            return True, "Departamento registrado."
        except Exception as error:
            return False, str(error)

    def get_department(self, department_name: str) -> tuple[Department | None, str | None]:
        """Return one department by name."""
        normalized_name = department_name.strip()
        department = self.__departments_by_name.get(normalized_name)
        return (department, None) if department is not None else (None, "No se encontró el departamento.")

    def list_departments(self) -> tuple[list[Department], str | None]:
        """Return all registered departments."""
        return self.__departments.copy(), None

    def add_location(self, department_name: str, location_address: str) -> tuple[bool, str]:
        """Add one location to the selected department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        location = DepartmentLocation(location_address.strip())
        return department.add_location(location)

    def list_locations(self, department_name: str) -> tuple[list[str] | None, str | None]:
        """Return all location addresses of one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return None, error_message if error_message is not None else "No se encontró el departamento."
        addresses = [location.get_address() for location in department.get_locations()]
        return addresses, None

    def assign_manager(self, department_name: str, manager_ssn: str) -> tuple[bool, str]:
        """Assign one manager SSN to one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        normalized_ssn = manager_ssn.strip()
        managed_department_name = self.__managed_department_by_manager_ssn.get(normalized_ssn)
        if managed_department_name is not None:
            return False, "Este gerente ya controla otro departamento."
        assigned, message = department.assign_manager(normalized_ssn)
        if assigned:
            self.__managed_department_by_manager_ssn[normalized_ssn] = department.get_name()
        return assigned, message

    def add_employee_to_department(self, department_name: str, employee_ssn: str) -> tuple[bool, str]:
        """Add employee SSN to one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        return department.add_employee_ssn(employee_ssn.strip())

    def add_project_to_department(self, department_name: str, project_name: str) -> tuple[bool, str]:
        """Add project name to one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        return department.add_project_name(project_name.strip())

    def remove_project_from_department(self, department_name: str, project_name: str) -> tuple[bool, str]:
        """Remove one project relation from one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        return department.remove_project_name(project_name.strip())

    def remove_employee_from_department(self, department_name: str, employee_ssn: str) -> tuple[bool, str]:
        """Remove one employee relation from one department."""
        department, error_message = self.get_department(department_name)
        if department is None:
            return False, error_message if error_message is not None else "No se encontró el departamento."
        normalized_ssn = employee_ssn.strip()
        removed, removed_message = department.remove_employee_ssn(normalized_ssn)
        if not removed:
            return False, removed_message
        if department.get_manager_ssn() == normalized_ssn:
            self.__managed_department_by_manager_ssn.pop(normalized_ssn, None)
            department.unassign_manager(normalized_ssn)
        return True, "Empleado desvinculado del departamento."

    def remove_department(self, department_name: str) -> tuple[bool, str]:
        """Remove one department if no employees or projects are linked."""
        try:
            department, error_message = self.get_department(department_name)
            if department is None:
                return False, error_message if error_message is not None else "No se encontró el departamento."
            if department.get_employee_ssns():
                return False, "No se puede eliminar un departamento con empleados."
            if department.get_project_names():
                return False, "No se puede eliminar un departamento con proyectos."
            manager_ssn = department.get_manager_ssn()
            self.__departments.remove(department)
            self.__departments_by_name.pop(department.get_name(), None)
            if manager_ssn is not None:
                self.__managed_department_by_manager_ssn.pop(manager_ssn, None)
            return True, "Departamento eliminado."
        except Exception as error:
            return False, str(error)
