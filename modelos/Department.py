from typing import Optional

from DepartmentLocation import DepartmentLocation


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
            return False, "Location already exists."
        self.__locations.append(location)
        return True, "Location added."

    def assign_manager(self, manager_ssn: str) -> tuple[bool, str]:
        """Assign one manager to the department."""
        if self.__manager_ssn is not None:
            return False, "Department already has a manager."
        self.__manager_ssn = manager_ssn
        return True, "Manager assigned."

    def add_employee_ssn(self, employee_ssn: str) -> tuple[bool, str]:
        """Add employee SSN to this department."""
        if employee_ssn in self.__employee_ssns:
            return False, "Employee already belongs to this department."
        self.__employee_ssns.append(employee_ssn)
        return True, "Employee assigned to department."

    def add_project_name(self, project_name: str) -> tuple[bool, str]:
        """Register a controlled project name."""
        if project_name in self.__project_names:
            return False, "Project is already controlled by this department."
        self.__project_names.append(project_name)
        return True, "Project assigned to department."
