# Checklist recomendado (paso a paso)

- [x] **1) Cerrar modelo de dominio base (`modelos/`)**
- [x] Crear/ajustar: `Department`, `Project`, `Person`, `Employee`, `Child`
- [x] Definir jerarquía de roles: `Manager`, `SalesRepresentative`, `Engineer`, `SalesEngineer`
- [x] Modelar relaciones obligatorias:
- [x] empleado -> 1 departamento
- [x] departamento -> muchos empleados
- [x] departamento -> 1 manager
- [x] departamento -> muchos proyectos
- [x] empleado -> muchos hijos
- [x] ingenieros/representantes -> proyectos (N:M)
- [x] Revisar consistencia base con el enunciado

- [ ] **2) Incluir comportamiento OO mínimo**
- [x] Método común polimórfico en `Employee` y subclases (`can_join_projects`)
- [x] Encapsulamiento consistente (atributos no públicos + acceso controlado)
- [x] Docstrings en clases y métodos públicos

- [ ] **3) Crear capa `servicios/` (lógica de negocio)**
- [ ] `servicio_departamentos.py`
- [ ] `servicio_empleados.py`
- [ ] `servicio_proyectos.py`
- [ ] `servicio_hijos.py`
- [ ] Todas las funciones con parámetros y retorno tipo `(ok, mensaje)` o `(resultado, error)`

- [ ] **4) Implementar reglas funcionales RF1-RF10**
- [ ] RF1: registrar departamentos sin duplicados
- [ ] RF2: ubicaciones por departamento (agregar/listar/sin repetidos)
- [ ] RF3: empleados con SSN único y departamento obligatorio
- [ ] RF4: clasificación por jerarquía de subclases
- [ ] RF5: un solo manager por departamento
- [ ] RF6: hijos con empleado existente y fecha válida
- [ ] RF7: proyectos con nombre único y departamento controlador
- [ ] RF8: participación solo roles permitidos
- [ ] RF9: consultas cruzadas clave
- [ ] RF10: validar antes de eliminar

- [ ] **5) Estructuras de datos reales**
- [ ] Listas para colecciones (empleados, proyectos, hijos)
- [ ] Diccionarios para índices (por `ssn`, nombre de proyecto, nombre departamento)

- [ ] **6) Crear interfaz de consola (`consola/`)**
- [ ] Menú principal + submenús
- [ ] `while` para ciclo principal
- [ ] `match-case` para opciones
- [ ] `if` para validaciones y decisiones
- [ ] `for` para listados y recorridos
- [ ] No salir hasta opción "Salir"

- [ ] **7) Manejo de excepciones**
- [ ] `try/except` en conversiones de entrada (int/float/fecha)
- [ ] `try/except` para operaciones inválidas de negocio

- [ ] **8) Paquete `utilidades/`**
- [ ] Validadores reutilizables (SSN, salario, fecha, no vacío, duplicados)
- [ ] Helpers de entrada/salida para desacoplar consola de servicios

- [ ] **9) Verificación final de evidencias obligatorias**
- [ ] Herencia observable
- [ ] Polimorfismo observable
- [ ] Encapsulamiento real
- [ ] Listas + diccionarios en uso real
- [ ] `while`, `for`, `if` y `match` en flujo funcional
- [ ] Excepciones aplicadas
- [ ] Separación en paquetes/módulos

- [ ] **10) Entregables**
- [ ] Diagrama de clases (UML o equivalente)
- [ ] Código fuente completo organizado
- [ ] Documento breve (arquitectura, herencia/polimorfismo, decisiones)

## Estado actual rápido

- [x] Inicio de `modelos/`
- [x] Encapsulamiento base
- [x] Herencia inicial y jerarquía de roles
- [x] Renombrado consistente a inglés en clases, atributos, métodos y archivos
- [ ] Servicios, menús y utilidades: pendiente
