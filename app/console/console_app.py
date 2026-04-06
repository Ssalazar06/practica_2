from services.child_service import ChildService
from services.department_service import DepartmentService
from services.employee_service import EmployeeService
from services.project_service import ProjectService
from utilities.io_helpers import print_error, print_section, print_success, read_menu_option, read_text
from utilities.validators import validate_iso_date, validate_non_empty_text, validate_positive_salary, validate_ssn


class ConsoleApp:
    """Run the console interface for the organization system."""

    def __init__(self):
        """Initialize services and service dependencies."""
        self.__department_service = DepartmentService()
        self.__project_service: ProjectService | None = None
        self.__employee_service = EmployeeService(
            self.__department_service.get_department,
            self.__department_service.add_employee_to_department,
            self.__department_service.remove_employee_from_department,
            self.__department_service.assign_manager,
            self.__find_employee_project_names,
        )
        self.__project_service = ProjectService(
            self.__department_service.get_department,
            self.__department_service.add_project_to_department,
            self.__department_service.remove_project_from_department,
            self.__employee_service.get_employee,
        )
        self.__child_service = ChildService(self.__employee_service.get_employee)

    def run(self) -> None:
        """Run main menu loop until user chooses exit."""
        keep_running = True
        while keep_running:
            self.__show_main_menu()
            option = self.__read_menu_option()
            match option:
                case 1:
                    self.__department_menu()
                case 2:
                    self.__employee_menu()
                case 3:
                    self.__child_menu()
                case 4:
                    self.__project_menu()
                case 5:
                    self.__query_menu()
                case 0:
                    keep_running = False
                    print("Programa finalizado.")
                case _:
                    print("Opción inválida.")

    def __show_main_menu(self) -> None:
        """Print main menu options."""
        print_section("Menú principal")
        print("1. Gestión de departamentos")
        print("2. Gestión de empleados")
        print("3. Gestión de hijos")
        print("4. Gestión de proyectos")
        print("5. Consultas")
        print("0. Salir")

    def __department_menu(self) -> None:
        """Run department submenu."""
        keep_running = True
        while keep_running:
            print_section("Menú de departamentos")
            print("1. Registrar departamento")
            print("2. Listar departamentos")
            print("3. Agregar ubicación")
            print("4. Listar ubicaciones")
            print("5. Eliminar departamento")
            print("0. Volver")
            option = self.__read_menu_option()
            match option:
                case 1:
                    self.__safe_execute(self.__register_department_flow)
                case 2:
                    departments, _ = self.__department_service.list_departments()
                    if not departments:
                        print_success("No hay departamentos registrados.")
                    for department in departments:
                        print(f"- {department.get_name()}")
                case 3:
                    self.__safe_execute(self.__add_location_flow)
                case 4:
                    department_name = read_text("Nombre del departamento: ")
                    locations, error = self.__department_service.list_locations(department_name)
                    if locations is None:
                        print_error(error)
                    elif not locations:
                        print_success("No hay ubicaciones registradas.")
                    else:
                        for location in locations:
                            print(f"- {location}")
                case 5:
                    self.__safe_execute(self.__remove_department_flow)
                case 0:
                    keep_running = False
                case _:
                    print("Opción inválida.")

    def __employee_menu(self) -> None:
        """Run employee submenu."""
        keep_running = True
        while keep_running:
            print_section("Menú de empleados")
            print("1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Listar empleados por departamento")
            print("4. Listar empleados por rol")
            print("5. Eliminar empleado")
            print("0. Volver")
            option = self.__read_menu_option()
            match option:
                case 1:
                    self.__safe_execute(self.__register_employee_flow)
                case 2:
                    employees, _ = self.__employee_service.list_employees()
                    if not employees:
                        print_success("No hay empleados registrados.")
                    for employee in employees:
                        role = self.__employee_service.get_employee_role_name(employee)
                        print(
                            f"- Documento: {employee.get_ssn()} | Nombre: {employee.get_full_name()} | Rol: {role}"
                        )
                case 3:
                    department_name = read_text("Nombre del departamento: ")
                    employees, _ = self.__employee_service.list_employees_by_department(department_name)
                    if not employees:
                        print_success("No se encontraron empleados.")
                    for employee in employees:
                        print(f"- {employee.get_ssn()} | {employee.get_full_name()}")
                case 4:
                    role_name = read_text(
                        "Rol (manager / sales_representative / engineer / sales_engineer): "
                    )
                    employees, error = self.__employee_service.list_employees_by_role(role_name)
                    if error is not None:
                        print_error(error)
                    elif not employees:
                        print_success("No se encontraron empleados.")
                    else:
                        for employee in employees:
                            print(f"- {employee.get_ssn()} | {employee.get_full_name()}")
                case 5:
                    self.__safe_execute(self.__remove_employee_flow)
                case 0:
                    keep_running = False
                case _:
                    print("Opción inválida.")

    def __child_menu(self) -> None:
        """Run child submenu."""
        keep_running = True
        while keep_running:
            print_section("Menú de hijos")
            print("1. Registrar hijo")
            print("2. Listar hijos por empleado")
            print("0. Volver")
            option = self.__read_menu_option()
            match option:
                case 1:
                    self.__safe_execute(self.__register_child_flow)
                case 2:
                    employee_ssn = self.__read_validated_ssn("Documento del empleado (solo números, máx. 9 dígitos): ")
                    if employee_ssn is None:
                        continue
                    children, error = self.__child_service.list_children_by_employee(employee_ssn)
                    if children is None:
                        print_error(error)
                    elif not children:
                        print_success("No hay hijos registrados.")
                    else:
                        for child in children:
                            print(f"- {child.get_name()} | {child.get_birth_date()}")
                case 0:
                    keep_running = False
                case _:
                    print("Opción inválida.")

    def __project_menu(self) -> None:
        """Run project submenu."""
        keep_running = True
        while keep_running:
            print_section("Menú de proyectos")
            print("1. Registrar proyecto")
            print("2. Listar proyectos")
            print("3. Listar proyectos por departamento")
            print("4. Asignar participante al proyecto")
            print("5. Listar participantes por proyecto")
            print("6. Listar proyectos por empleado")
            print("7. Eliminar proyecto")
            print("0. Volver")
            option = self.__read_menu_option()
            match option:
                case 1:
                    self.__safe_execute(self.__register_project_flow)
                case 2:
                    projects, _ = self.__project_service.list_projects()
                    if not projects:
                        print_success("No hay proyectos registrados.")
                    for project in projects:
                        print(
                            f"- {project.get_name()} | {project.get_start_date()} | Departamento: "
                            f"{project.get_controlling_department_name()}"
                        )
                case 3:
                    department_name = read_text("Nombre del departamento: ")
                    projects, _ = self.__project_service.list_projects_by_department(department_name)
                    if not projects:
                        print_success("No se encontraron proyectos.")
                    for project in projects:
                        print(f"- {project.get_name()} | {project.get_start_date()}")
                case 4:
                    self.__safe_execute(self.__assign_participant_flow)
                case 5:
                    project_name = read_text("Nombre del proyecto: ")
                    participants, error = self.__project_service.list_participants_by_project(project_name)
                    if participants is None:
                        print_error(error)
                    elif not participants:
                        print_success("No hay participantes registrados.")
                    else:
                        for participant in participants:
                            print(f"- {participant.get_ssn()} | {participant.get_full_name()}")
                case 6:
                    employee_ssn = self.__read_validated_ssn("Documento del empleado (solo números, máx. 9 dígitos): ")
                    if employee_ssn is None:
                        continue
                    projects, error = self.__project_service.list_projects_by_employee(employee_ssn)
                    if projects is None:
                        print_error(error)
                    elif not projects:
                        print_success("No se encontraron proyectos.")
                    else:
                        for project in projects:
                            print(f"- {project.get_name()} | {project.get_start_date()}")
                case 7:
                    self.__safe_execute(self.__remove_project_flow)
                case 0:
                    keep_running = False
                case _:
                    print("Opción inválida.")

    def __query_menu(self) -> None:
        """Run additional query submenu."""
        keep_running = True
        while keep_running:
            print_section("Menú de consultas")
            print("1. Empleados por departamento")
            print("2. Proyectos por departamento")
            print("3. Proyectos por empleado")
            print("4. Hijos por empleado")
            print("0. Volver")
            option = self.__read_menu_option()
            match option:
                case 1:
                    department_name = read_text("Nombre del departamento: ")
                    employees, _ = self.__employee_service.list_employees_by_department(department_name)
                    if not employees:
                        print_success("No se encontraron empleados.")
                    for employee in employees:
                        print(f"- {employee.get_ssn()} | {employee.get_full_name()}")
                case 2:
                    department_name = read_text("Nombre del departamento: ")
                    projects, _ = self.__project_service.list_projects_by_department(department_name)
                    if not projects:
                        print_success("No se encontraron proyectos.")
                    for project in projects:
                        print(f"- {project.get_name()} | {project.get_start_date()}")
                case 3:
                    employee_ssn = self.__read_validated_ssn("Documento del empleado (solo números, máx. 9 dígitos): ")
                    if employee_ssn is None:
                        continue
                    projects, error = self.__project_service.list_projects_by_employee(employee_ssn)
                    if projects is None:
                        print_error(error)
                    elif not projects:
                        print_success("No se encontraron proyectos.")
                    else:
                        for project in projects:
                            print(f"- {project.get_name()} | {project.get_start_date()}")
                case 4:
                    employee_ssn = self.__read_validated_ssn("Documento del empleado (solo números, máx. 9 dígitos): ")
                    if employee_ssn is None:
                        continue
                    children, error = self.__child_service.list_children_by_employee(employee_ssn)
                    if children is None:
                        print_error(error)
                    elif not children:
                        print_success("No se encontraron hijos.")
                    else:
                        for child in children:
                            print(f"- {child.get_name()} | {child.get_birth_date()}")
                case 0:
                    keep_running = False
                case _:
                    print("Opción inválida.")

    def __register_employee_flow(self) -> None:
        """Capture employee data and register it."""
        role_name = read_text(
            "Rol (manager / sales_representative / engineer / sales_engineer): "
        ).strip().lower()
        ssn_raw = read_text("Documento / identificador (solo números, máx. 9 dígitos): ")
        ssn, ssn_error = validate_ssn(ssn_raw)
        if ssn is None:
            print_error(ssn_error)
            return
        salary, salary_error = validate_positive_salary(read_text("Salario: "))
        if salary is None:
            print_error(salary_error)
            return
        department_name, department_error = validate_non_empty_text(
            read_text("Nombre del departamento: "), "El nombre del departamento"
        )
        if department_name is None:
            print_error(department_error)
            return
        person_id, person_id_error = validate_non_empty_text(
            read_text("Identificador de persona: "), "El identificador de persona"
        )
        if person_id is None:
            print_error(person_id_error)
            return
        first_name, first_name_error = validate_non_empty_text(read_text("Primer nombre: "), "El primer nombre")
        if first_name is None:
            print_error(first_name_error)
            return
        middle_name = read_text("Segundo nombre (opcional): ").strip()
        last_name, last_name_error = validate_non_empty_text(read_text("Primer apellido: "), "El primer apellido")
        if last_name is None:
            print_error(last_name_error)
            return
        second_last_name = read_text("Segundo apellido (opcional): ").strip()
        birth_date, birth_date_error = validate_iso_date(
            read_text("Fecha de nacimiento (AAAA-MM-DD): "), "la fecha de nacimiento"
        )
        if birth_date is None:
            print_error(birth_date_error)
            return
        employee, error = self.__employee_service.register_employee(
            role_name,
            ssn,
            salary,
            department_name,
            person_id,
            first_name,
            middle_name,
            last_name,
            second_last_name,
            birth_date,
        )
        print_success("Empleado registrado.") if employee is not None else print_error(error)

    def __register_department_flow(self) -> None:
        """Capture and register department."""
        department_name, error = validate_non_empty_text(
            read_text("Nombre del departamento: "), "El nombre del departamento"
        )
        if department_name is None:
            print_error(error)
            return
        ok, message = self.__department_service.register_department(department_name)
        print_success(message) if ok else print_error(message)

    def __add_location_flow(self) -> None:
        """Capture and add one location."""
        department_name, department_error = validate_non_empty_text(
            read_text("Nombre del departamento: "), "El nombre del departamento"
        )
        if department_name is None:
            print_error(department_error)
            return
        location, location_error = validate_non_empty_text(
            read_text("Dirección de la ubicación: "), "La dirección de la ubicación"
        )
        if location is None:
            print_error(location_error)
            return
        ok, message = self.__department_service.add_location(department_name, location)
        print_success(message) if ok else print_error(message)

    def __remove_department_flow(self) -> None:
        """Capture and remove department."""
        department_name, error = validate_non_empty_text(
            read_text("Nombre del departamento: "), "El nombre del departamento"
        )
        if department_name is None:
            print_error(error)
            return
        ok, message = self.__department_service.remove_department(department_name)
        print_success(message) if ok else print_error(message)

    def __remove_employee_flow(self) -> None:
        """Capture and remove employee."""
        ssn, error = validate_ssn(read_text("Documento del empleado (solo números, máx. 9 dígitos): "))
        if ssn is None:
            print_error(error)
            return
        ok, message = self.__employee_service.remove_employee(ssn)
        print_success(message) if ok else print_error(message)

    def __register_child_flow(self) -> None:
        """Capture and register child."""
        employee_ssn, ssn_error = validate_ssn(
            read_text("Documento del empleado (solo números, máx. 9 dígitos): ")
        )
        if employee_ssn is None:
            print_error(ssn_error)
            return
        child_name, child_error = validate_non_empty_text(read_text("Nombre del hijo: "), "El nombre del hijo")
        if child_name is None:
            print_error(child_error)
            return
        birth_date_text = read_text("Fecha de nacimiento del hijo (AAAA-MM-DD): ")
        child, error = self.__child_service.register_child(employee_ssn, child_name, birth_date_text)
        print_success("Hijo registrado.") if child is not None else print_error(error)

    def __register_project_flow(self) -> None:
        """Capture and register project."""
        project_name, project_error = validate_non_empty_text(
            read_text("Nombre del proyecto: "), "El nombre del proyecto"
        )
        if project_name is None:
            print_error(project_error)
            return
        start_date_text = read_text("Fecha de inicio (AAAA-MM-DD): ")
        _, date_error = validate_iso_date(start_date_text, "la fecha de inicio")
        if date_error is not None:
            print_error(date_error)
            return
        department_name, department_error = validate_non_empty_text(
            read_text("Departamento controlador: "), "El departamento controlador"
        )
        if department_name is None:
            print_error(department_error)
            return
        project, error = self.__project_service.register_project(project_name, start_date_text, department_name)
        print_success("Proyecto registrado.") if project is not None else print_error(error)

    def __assign_participant_flow(self) -> None:
        """Capture and assign one project participant."""
        project_name, project_error = validate_non_empty_text(
            read_text("Nombre del proyecto: "), "El nombre del proyecto"
        )
        if project_name is None:
            print_error(project_error)
            return
        employee_ssn, ssn_error = validate_ssn(
            read_text("Documento del empleado (solo números, máx. 9 dígitos): ")
        )
        if employee_ssn is None:
            print_error(ssn_error)
            return
        ok, message = self.__project_service.assign_participant_by_ssn(project_name, employee_ssn)
        print_success(message) if ok else print_error(message)

    def __remove_project_flow(self) -> None:
        """Capture and remove one project."""
        project_name, error = validate_non_empty_text(
            read_text("Nombre del proyecto: "), "El nombre del proyecto"
        )
        if project_name is None:
            print_error(error)
            return
        ok, message = self.__project_service.remove_project(project_name)
        print_success(message) if ok else print_error(message)

    def __find_employee_project_names(self, employee_ssn: str) -> tuple[list[str] | None, str | None]:
        """Return project names assigned to one employee."""
        return self.__project_service.list_project_names_by_employee(employee_ssn) if self.__project_service else ([], None)

    def __read_validated_ssn(self, prompt: str) -> str | None:
        """Read document input and apply SSN validation rules."""
        ssn, error = validate_ssn(read_text(prompt))
        if ssn is None:
            print_error(error)
            return None
        return ssn

    def __read_menu_option(self) -> int:
        """Read numeric menu option with exception handling."""
        option, error = read_menu_option()
        if error is not None:
            print_error(error)
            return -1
        return option if option is not None else -1

    def __safe_execute(self, callback) -> None:
        """Execute one action and capture unexpected errors."""
        try:
            callback()
        except Exception as error:
            print_error(str(error))
