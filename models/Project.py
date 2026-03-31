from datetime import date


class Project:
    """Represents one project controlled by one department."""

    __name: str
    __start_date: date
    __controlling_department_name: str
    __participant_ssns: list[str]

    def __init__(self, name: str, start_date: date, controlling_department_name: str):
        """Initialize one project with its required fields."""
        self.__name = name
        self.__start_date = start_date
        self.__controlling_department_name = controlling_department_name
        self.__participant_ssns = []

    def get_name(self) -> str:
        """Return project name."""
        return self.__name

    def get_start_date(self) -> date:
        """Return project start date."""
        return self.__start_date

    def get_controlling_department_name(self) -> str:
        """Return department name controlling this project."""
        return self.__controlling_department_name

    def get_participant_ssns(self) -> list[str]:
        """Return participant SSNs."""
        return self.__participant_ssns

    def set_name(self, name: str) -> None:
        """Update project name."""
        self.__name = name

    def set_start_date(self, start_date: date) -> None:
        """Update project start date."""
        self.__start_date = start_date

    def add_participant(self, employee_ssn: str) -> tuple[bool, str]:
        """Add participant SSN if not duplicated."""
        if employee_ssn in self.__participant_ssns:
            return False, "Employee already assigned to this project."
        self.__participant_ssns.append(employee_ssn)
        return True, "Participant assigned."
