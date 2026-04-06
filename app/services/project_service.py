from datetime import date
from typing import Callable

from models.department import Department
from models.person import Employee, Engineer, SalesEngineer, SalesRepresentative
from models.project import Project


class ProjectService:
    """Handle project business operations."""

    def __init__(
        self,
        find_department: Callable[[str], tuple[Department | None, str | None]],
        link_project_to_department: Callable[[str, str], tuple[bool, str]],
        unlink_project_from_department: Callable[[str, str], tuple[bool, str]],
        find_employee: Callable[[str], tuple[Employee | None, str | None]],
    ):
        """Initialize project service with required dependencies."""
        self.__find_department = find_department
        self.__link_project_to_department = link_project_to_department
        self.__unlink_project_from_department = unlink_project_from_department
        self.__find_employee = find_employee
        self.__projects: list[Project] = []
        self.__projects_by_name: dict[str, Project] = {}

    def register_project(
        self, project_name: str, start_date_text: str, controlling_department_name: str
    ) -> tuple[Project | None, str | None]:
        """Register one project with unique name and valid date."""
        try:
            normalized_name = project_name.strip()
            if normalized_name in self.__projects_by_name:
                return None, "Ya existe un proyecto con ese nombre."

            department, error_message = self.__find_department(controlling_department_name.strip())
            if department is None:
                return None, error_message if error_message is not None else "No se encontró el departamento."

            parsed_date, parsed_date_error = self.parse_date(start_date_text)
            if parsed_date is None:
                return None, parsed_date_error

            project = Project(normalized_name, parsed_date, department.get_name())
            self.__projects.append(project)
            self.__projects_by_name[normalized_name] = project
            self.__link_project_to_department(department.get_name(), normalized_name)
            return project, None
        except Exception as error:
            return None, str(error)

    def get_project(self, project_name: str) -> tuple[Project | None, str | None]:
        """Return one project by name."""
        project = self.__projects_by_name.get(project_name.strip())
        return (project, None) if project is not None else (None, "No se encontró el proyecto.")

    def list_projects(self) -> tuple[list[Project], str | None]:
        """Return all registered projects."""
        return self.__projects.copy(), None

    def assign_participant(self, project_name: str, employee: Employee) -> tuple[bool, str]:
        """Assign one participant when role is allowed."""
        project, error_message = self.get_project(project_name.strip())
        if project is None:
            return False, error_message if error_message is not None else "No se encontró el proyecto."
        if not employee.can_join_projects():
            return False, "El rol de este empleado no puede unirse a proyectos."
        if project.get_controlling_department_name() != employee.get_department().get_name():
            return False, "El empleado pertenece a otro departamento."
        if not isinstance(employee, (Engineer, SalesRepresentative, SalesEngineer)):
            return False, "Solo roles de ingeniería o ventas pueden unirse al proyecto."
        return project.add_participant(employee.get_ssn())

    def assign_participant_by_ssn(self, project_name: str, employee_ssn: str) -> tuple[bool, str]:
        """Assign participant by SSN."""
        try:
            employee, error_message = self.__find_employee(employee_ssn.strip())
            if employee is None:
                return False, error_message if error_message is not None else "No se encontró el empleado."
            return self.assign_participant(project_name, employee)
        except Exception as error:
            return False, str(error)

    def list_projects_by_department(self, department_name: str) -> tuple[list[Project], str | None]:
        """Return projects controlled by one department."""
        filtered_projects = [
            project
            for project in self.__projects
            if project.get_controlling_department_name().lower() == department_name.strip().lower()
        ]
        return filtered_projects, None

    def list_participants_by_project(self, project_name: str) -> tuple[list[Employee] | None, str | None]:
        """Return project participants as employee objects."""
        project, error_message = self.get_project(project_name.strip())
        if project is None:
            return None, error_message if error_message is not None else "No se encontró el proyecto."
        participant_employees: list[Employee] = []
        for ssn in project.get_participant_ssns():
            employee, _ = self.__find_employee(ssn)
            if employee is not None:
                participant_employees.append(employee)
        return participant_employees, None

    def list_projects_by_employee(self, employee_ssn: str) -> tuple[list[Project] | None, str | None]:
        """Return projects where one employee participates."""
        employee, error_message = self.__find_employee(employee_ssn.strip())
        if employee is None:
            return None, error_message if error_message is not None else "No se encontró el empleado."
        employee_projects = [project for project in self.__projects if employee.get_ssn() in project.get_participant_ssns()]
        return employee_projects, None

    def list_project_names_by_employee(self, employee_ssn: str) -> tuple[list[str] | None, str | None]:
        """Return project names where one employee participates."""
        projects, error_message = self.list_projects_by_employee(employee_ssn)
        if projects is None:
            return None, error_message if error_message is not None else "No se encontró el empleado."
        project_names = [project.get_name() for project in projects]
        return project_names, None

    def remove_project(self, project_name: str) -> tuple[bool, str]:
        """Remove one project and unlink it from department."""
        project, error_message = self.get_project(project_name.strip())
        if project is None:
            return False, error_message if error_message is not None else "No se encontró el proyecto."
        unlinked, unlink_message = self.__unlink_project_from_department(
            project.get_controlling_department_name(), project.get_name()
        )
        if not unlinked:
            return False, unlink_message
        self.__projects.remove(project)
        self.__projects_by_name.pop(project.get_name(), None)
        return True, "Proyecto eliminado."

    def parse_date(self, date_text: str) -> tuple[date | None, str | None]:
        """Parse date using ISO format YYYY-MM-DD."""
        try:
            parsed_date = date.fromisoformat(date_text.strip())
            return parsed_date, None
        except ValueError:
            return None, "Formato de fecha inválido. Use AAAA-MM-DD."
