from typing import Optional

from models.department_location import DepartmentLocation


class Department:
    """Represents one department in the organization."""

    __name: str
    __locations: list[DepartmentLocation]
    __manager_ssn: Optional[str]
    __employee_ssns: list[str]
    __project_names: list[str]

    def __init__(self, name: str):
        """Initialize a department with required name."""
        self.__name = name
        self.__locations = []
        self.__manager_ssn = None
        self.__employee_ssns = []
        self.__project_names = []

    def get_name(self) -> str:
        """Return the department name."""
        return self.__name

    def get_locations(self) -> list[DepartmentLocation]:
        """Return the department locations."""
        return self.__locations

    def get_manager_ssn(self) -> Optional[str]:
        """Return manager SSN if assigned."""
        return self.__manager_ssn

    def get_employee_ssns(self) -> list[str]:
        """Return employee SSNs assigned to this department."""
        return self.__employee_ssns

    def get_project_names(self) -> list[str]:
        """Return project names controlled by this department."""
        return self.__project_names

    def set_name(self, name: str) -> None:
        """Update the department name."""
        self.__name = name

    def add_location(self, location: DepartmentLocation) -> tuple[bool, str]:
        """Add one location if it does not exist yet."""
        location_addresses = [item.get_address() for item in self.__locations]
        if location.get_address() in location_addresses:
            return False, "Esa ubicación ya existe."
        self.__locations.append(location)
        return True, "Ubicación agregada."

    def assign_manager(self, manager_ssn: str) -> tuple[bool, str]:
        """Assign one manager to the department."""
        if self.__manager_ssn is not None:
            return False, "El departamento ya tiene un gerente asignado."
        self.__manager_ssn = manager_ssn
        return True, "Gerente asignado."

    def unassign_manager(self, manager_ssn: str) -> tuple[bool, str]:
        """Clear manager assignment if SSN matches current manager."""
        if self.__manager_ssn is None:
            return False, "El departamento no tiene gerente asignado."
        if self.__manager_ssn != manager_ssn:
            return False, "El documento del gerente no coincide con el gerente actual."
        self.__manager_ssn = None
        return True, "Gerente desasignado."

    def add_employee_ssn(self, employee_ssn: str) -> tuple[bool, str]:
        """Add employee SSN to this department."""
        if employee_ssn in self.__employee_ssns:
            return False, "El empleado ya pertenece a este departamento."
        self.__employee_ssns.append(employee_ssn)
        return True, "Empleado asignado al departamento."

    def remove_employee_ssn(self, employee_ssn: str) -> tuple[bool, str]:
        """Remove employee SSN from this department."""
        if employee_ssn not in self.__employee_ssns:
            return False, "El empleado no pertenece a este departamento."
        self.__employee_ssns.remove(employee_ssn)
        return True, "Empleado retirado del departamento."

    def add_project_name(self, project_name: str) -> tuple[bool, str]:
        """Register a controlled project name."""
        if project_name in self.__project_names:
            return False, "El proyecto ya está controlado por este departamento."
        self.__project_names.append(project_name)
        return True, "Proyecto asignado al departamento."

    def remove_project_name(self, project_name: str) -> tuple[bool, str]:
        """Remove project name from this department."""
        if project_name not in self.__project_names:
            return False, "El proyecto no está controlado por este departamento."
        self.__project_names.remove(project_name)
        return True, "Proyecto retirado del departamento."
