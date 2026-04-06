from datetime import date
from typing import Callable

from models.child import Child
from models.person import Employee


class ChildService:
    """Handle child registration and related queries."""

    def __init__(self, find_employee: Callable[[str], tuple[Employee | None, str | None]]):
        """Initialize child service with employee dependency."""
        self.__find_employee = find_employee
        self.__children: list[Child] = []

    def register_child(self, employee_ssn: str, child_name: str, birth_date_text: str) -> tuple[Child | None, str | None]:
        """Register one child for an existing employee."""
        try:
            employee, error_message = self.__find_employee(employee_ssn.strip())
            if employee is None:
                return None, error_message if error_message is not None else "No se encontró el empleado."

            parsed_date, parsed_date_error = self.parse_date(birth_date_text)
            if parsed_date is None:
                return None, parsed_date_error

            child = Child(child_name.strip(), parsed_date, employee.get_ssn())
            added, added_message = employee.add_child(child)
            if not added:
                return None, added_message
            self.__children.append(child)
            return child, None
        except Exception as error:
            return None, str(error)

    def list_children_by_employee(self, employee_ssn: str) -> tuple[list[Child] | None, str | None]:
        """Return children of one employee."""
        employee, error_message = self.__find_employee(employee_ssn.strip())
        if employee is None:
            return None, error_message if error_message is not None else "No se encontró el empleado."
        return employee.get_children().copy(), None

    def parse_date(self, date_text: str) -> tuple[date | None, str | None]:
        """Parse date using ISO format YYYY-MM-DD."""
        try:
            parsed_date = date.fromisoformat(date_text.strip())
            return parsed_date, None
        except ValueError:
            return None, "Formato de fecha inválido. Use AAAA-MM-DD."
