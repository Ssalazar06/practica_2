import sys
from app.services.OrganizationService import OrganizationService
from utils.ValidationUtils import ValidationUtils


def main_menu():
    service = OrganizationService()

    while True:
        print("\n--- SISTEMA DE GESTIÓN ORGANIZACIONAL ---")
        print("1. Gestión de Departamentos")
        print("2. Gestión de Empleados (Personas)")
        print("3. Gestión de Proyectos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        match opcion: # Estructura match-case exigida 
            case "1":
                submenu_departments(service)
            case "2":
                submenu_employees(service)
            case "3":
                submenu_projects(service)
            case "4":
                print("Saliendo del sistema...")
                break # Finaliza el programa según el Requisito 2 [cite: 87]
            case _:
                print("Opción no válida.")

def submenu_departments(service):
    while True:
        print("\n--- GESTIÓN DE DEPARTAMENTOS ---")
        print("1. Crear Departamento")
        print("2. Agregar Ubicación a Departamento")
        print("3. Consultar Departamentos")
        print("99. Volver al Menú Principal")
        
        opc = input("Seleccione una opción: ")

        match opc:
            case "1":
                name = input("Ingrese el nombre del departamento: ")
                success, message = service.register_department(name)
                print(message)
            case "2":
                dept_name = input("Ingrese el nombre del departamento: ")
                address = input("Ingrese la nueva ubicación: ")
                success, message = service.add_location_to_department(dept_name, address)
                print(message)
            case "3":
                departments = service.get_all_departments()
                for dept in departments:
                    print(f"- {dept.name}")
            case "99":
                break
            case _:
                print("Opción no válida.")

