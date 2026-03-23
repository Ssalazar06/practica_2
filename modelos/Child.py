from datetime import date


class Child:
    """Represents one child of an employee."""

    __name: str
    __birth_date: date
    __employee_ssn: str

    def __init__(self, name: str, birth_date: date, employee_ssn: str):
        """Initialize child data."""
        self.__name = name
        self.__birth_date = birth_date
        self.__employee_ssn = employee_ssn

    def get_name(self) -> str:
        """Return child name."""
        return self.__name

    def get_birth_date(self) -> date:
        """Return child birth date."""
        return self.__birth_date

    def get_employee_ssn(self) -> str:
        """Return SSN of the parent employee."""
        return self.__employee_ssn
