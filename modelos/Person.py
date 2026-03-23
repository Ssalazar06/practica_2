from datetime import date

from Child import Child
from Department import Department
from Project import Project
from Specialization import Specialization


class Person:
    """Represents base personal data."""

    __person_id: str
    __first_name: str
    __middle_name: str
    __last_name: str
    __second_last_name: str
    __birth_date: date

    def __init__(
        self,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ):
        """Initialize personal identity fields."""
        self.__person_id = person_id
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__second_last_name = second_last_name
        self.__birth_date = birth_date

    def get_person_id(self) -> str:
        """Return person identifier."""
        return self.__person_id

    def get_first_name(self) -> str:
        """Return first name."""
        return self.__first_name

    def get_middle_name(self) -> str:
        """Return middle name."""
        return self.__middle_name

    def get_last_name(self) -> str:
        """Return last name."""
        return self.__last_name

    def get_second_last_name(self) -> str:
        """Return second last name."""
        return self.__second_last_name

    def get_birth_date(self) -> date:
        """Return birth date."""
        return self.__birth_date

    def get_full_name(self) -> str:
        """Return complete name."""
        return f"{self.__first_name} {self.__middle_name} {self.__last_name} {self.__second_last_name}".strip()


class Employee(Person):
    """Represents base employee behavior and data."""

    __ssn: str
    __salary: float
    __department: Department
    __children: list[Child]

    def __init__(
        self,
        ssn: str,
        salary: float,
        department: Department,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ):
        """Initialize employee information."""
        super().__init__(person_id, first_name, middle_name, last_name, second_last_name, birth_date)
        self.__ssn = ssn
        self.__salary = salary
        self.__department = department
        self.__children = []

    def get_ssn(self) -> str:
        """Return employee SSN."""
        return self.__ssn

    def get_salary(self) -> float:
        """Return employee salary."""
        return self.__salary

    def get_department(self) -> Department:
        """Return employee department."""
        return self.__department

    def get_children(self) -> list[Child]:
        """Return employee children."""
        return self.__children

    def set_salary(self, salary: float) -> None:
        """Update employee salary."""
        self.__salary = salary

    def add_child(self, child: Child) -> tuple[bool, str]:
        """Add one child to the employee."""
        child_names = [item.get_name() for item in self.__children]
        if child.get_name() in child_names:
            return False, "Child already registered for this employee."
        self.__children.append(child)
        return True, "Child added."

    def can_join_projects(self) -> bool:
        """Define if role can join projects."""
        return False


class Manager(Employee):
    """Represents one manager role."""

    def can_join_projects(self) -> bool:
        """Manager cannot join projects by default. Polimorfismo"""
        return False


class SalesRepresentative(Employee):
    """Represents a sales representative."""

    __regions: list[str]

    def __init__(
        self,
        ssn: str,
        salary: float,
        department: Department,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ):
        """Initialize sales representative."""
        super().__init__(ssn, salary, department, person_id, first_name, middle_name, last_name, second_last_name, birth_date)
        self.__regions = []

    def get_regions(self) -> list[str]:
        """Return assigned regions."""
        return self.__regions

    def add_region(self, region: str) -> tuple[bool, str]:
        """Add region if not repeated."""
        if region in self.__regions:
            return False, "Region already assigned."
        self.__regions.append(region)
        return True, "Region assigned."

    def can_join_projects(self) -> bool:
        """Sales representative can join projects."""
        return True


class Engineer(Employee):
    """Represents an engineer."""

    __specialties: list[Specialization]
    __projects: list[Project]

    def __init__(
        self,
        ssn: str,
        salary: float,
        department: Department,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ):
        """Initialize engineer."""
        super().__init__(ssn, salary, department, person_id, first_name, middle_name, last_name, second_last_name, birth_date)
        self.__specialties = []
        self.__projects = []

    def get_specialties(self) -> list[Specialization]:
        """Return engineer specialties."""
        return self.__specialties

    def get_projects(self) -> list[Project]:
        """Return engineer projects."""
        return self.__projects

    def add_specialty(self, specialty: Specialization) -> tuple[bool, str]:
        """Add specialty if not repeated."""
        specialty_names = [item.get_name() for item in self.__specialties]
        if specialty.get_name() in specialty_names:
            return False, "Specialty already assigned."
        self.__specialties.append(specialty)
        return True, "Specialty assigned."

    def assign_project(self, project: Project) -> tuple[bool, str]:
        """Assign project if not repeated."""
        project_names = [item.get_name() for item in self.__projects]
        if project.get_name() in project_names:
            return False, "Project already assigned."
        self.__projects.append(project)
        return True, "Project assigned."

    def can_join_projects(self) -> bool:
        """Engineer can join projects."""
        return True


class SalesEngineer(Engineer):
    """Represents a sales engineer."""

    __regions: list[str]

    def __init__(
        self,
        ssn: str,
        salary: float,
        department: Department,
        person_id: str,
        first_name: str,
        middle_name: str,
        last_name: str,
        second_last_name: str,
        birth_date: date,
    ):
        """Initialize sales engineer."""
        super().__init__(ssn, salary, department, person_id, first_name, middle_name, last_name, second_last_name, birth_date)
        self.__regions = []

    def get_regions(self) -> list[str]:
        """Return sales engineer regions."""
        return self.__regions

    def add_region(self, region: str) -> tuple[bool, str]:
        """Add one region if not repeated."""
        if region in self.__regions:
            return False, "Region already assigned."
        self.__regions.append(region)
        return True, "Region assigned."
