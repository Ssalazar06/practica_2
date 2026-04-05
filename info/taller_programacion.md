# Taller de Programación — Construcción de Bases de Datos I

## Propósito

A partir de un enunciado de dominio, el estudiante debe ser capaz de:
- Abstraer un **modelo orientado a objetos**
- Diseñar un **modelo de clases**
- Construir una **implementación funcional en Python** con arquitectura modular

Se evalúa la capacidad de pasar de la descripción del problema a una solución consistente, robusta y mantenible.

---

## Descripción General

Diseñar e implementar un programa en **Python 3.10+** que funcione en consola mediante menús.

La actividad consiste en:
- Derivar un modelo de clases coherente con el dominio
- Implementar el sistema utilizando **Programación Orientada a Objetos (POO)**
- Estructurar el código mediante **módulos y paquetes**
- Construir una interacción funcional mediante **menús en consola**

El desarrollo debe reflejar correspondencia lógica entre: interpretación del problema → diseño de clases → implementación.

---

## Problema (Dominio)

Una organización estructura su información alrededor de **departamentos**, **empleados**, **proyectos** e **hijos de los empleados**.

- Cada **departamento** se identifica por su nombre y puede estar asociado a uno o varios **lugares físicos (locaciones)**.
- Todo empleado debe estar vinculado a un **único departamento**; un departamento puede tener **múltiples empleados**.
- Existe el rol de **administrador (manager)**: es un tipo particular de empleado. Cada departamento es administrado por un manager, y un manager administra un solo departamento.
- Los **empleados** se identifican por su **SSN** y poseen: nombre (primer nombre, segundo nombre, primer apellido, segundo apellido) y **salario**.
- Algunos empleados pueden tener uno o varios **hijos**. Cada hijo posee nombre y fecha de nacimiento. Un hijo pertenece a un único empleado.

### Jerarquía de empleados

Los empleados se clasifican en los siguientes subtipos:

| Subtipo | Atributo adicional |
|---|---|
| Administrador | — |
| Representante de Ventas | Una o varias **regiones** |
| Ingeniero | Una o varias **especialidades** |
| Ingeniero de Ventas | Combina Representante de Ventas + Ingeniero |

### Proyectos

- Se identifican por **nombre** y poseen una **fecha de inicio**.
- Los ingenieros participan en proyectos (relación muchos a muchos).
- Un departamento puede controlar múltiples proyectos; cada proyecto es controlado por **un único departamento**.

> **Nota:** El enunciado es la fuente de verdad. No se permite introducir supuestos que no se deriven del texto.

---

## 1. Diseño — Modelo de Clases

Elaborar un modelo de clases (UML o notación equivalente) que incluya:

- Clases con sus **atributos y métodos** principales
- **Relaciones** entre clases: asociación, composición/agregación, herencia
- Evidencia explícita de los principios de POO:
  - **Abstracción:** clases y responsabilidades claras
  - **Encapsulamiento:** convención `_`/`__` y/o propiedades
  - **Herencia:** jerarquía de especialización
  - **Polimorfismo:** método común redefinido en subclases

**Entrega:** diagrama + breve explicación (máx. 1 página) justificando las decisiones principales de diseño.

---

## 2. Implementación

### Requisito 1 — Arquitectura modular

Organizar el proyecto en paquetes y módulos. Como mínimo:

- Paquete `modelos/` — clases del dominio
- Paquete `servicios/` — lógica de negocio (registrar, buscar, asignar, listar, etc.)
- Módulo `consola` — menús y entrada/salida
- Módulo `utilidades` — validaciones y apoyos reutilizables

Debe evidenciarse el uso de `imports` entre módulos y el **desacoplamiento** entre interfaz y lógica.

### Requisito 2 — Menús en consola

- Menú principal y submenús coherentes
- El programa no debe finalizar hasta que el usuario seleccione "Salir"

### Requisito 3 — Funciones con parámetros y retorno

Las funciones deben:
- Recibir parámetros (no todo puede ser `input()` directo)
- Retornar uno o dos valores — por ejemplo: `(ok, mensaje)` o `(resultado, error)`

### Requisito 4 — Estructuras de datos

- **Listas** para colecciones de objetos (empleados, proyectos, etc.)
- **Diccionarios** para indexación/búsqueda eficiente (por ejemplo, por SSN o por nombre de proyecto)

### Requisito 5 — Control de flujo

Evidenciar de forma verificable:
- `while` — control del menú
- `for` — recorridos y listados
- `if` — validaciones y decisiones
- `match-case` — selección de opciones del menú

### Requisito 6 — Manejo de excepciones

Usar `try/except` en al menos:
- Conversión de tipos (ej. salario, selección numérica del menú)
- Operaciones inválidas (buscar SSN inexistente, asignar proyecto a rol no permitido, etc.)

---

## 3. Operaciones Mínimas del Sistema

### 3.1 Gestión de Departamentos
- Registrar y consultar departamentos
- Administrar ubicaciones (locations)

### 3.2 Gestión de Empleados
- Registrar empleados
- Listar y consultar empleados
- Manejar roles especializados mediante la jerarquía de clases

### 3.3 Gestión de Dependientes (Hijos)
- Registrar hijos asociados a un empleado
- Listar hijos por empleado

### 3.4 Gestión de Proyectos
- Registrar proyectos
- Asociar/controlar proyectos por departamento

### 3.5 Participación en Proyectos
- Asignar participación en proyectos según el rol
- Listar participantes de un proyecto y proyectos de un participante

> Cada operación debe reflejarse en el menú y estar **operativa** (no solo definida).

---

## 4. Evidencias Obligatorias en el Código

Se verificará explícitamente que el proyecto incluya:

- [ ] Jerarquía de clases con herencia
- [ ] Al menos un caso observable de polimorfismo
- [ ] Encapsulamiento (atributos no públicos y acceso controlado)
- [ ] Uso real de listas y diccionarios
- [ ] Uso real de `while`, `for`, `if` y `match`
- [ ] Manejo de excepciones aplicable a entradas y operaciones
- [ ] Separación en paquetes/módulos

---

## 5. Requisitos Funcionales

| ID | Descripción |
|---|---|
| RF1 | Registrar departamentos sin nombres duplicados |
| RF2 | Gestionar ubicaciones por departamento: agregar, listar, evitar repetidos |
| RF3 | Registrar empleados con SSN único y departamento obligatorio |
| RF4 | Clasificar empleados como: Administrador, Representante de Ventas, Ingeniero, Ingeniero de Ventas |
| RF5 | Un departamento solo puede tener **un manager** asignado |
| RF6 | Registrar hijos con asociación a empleado existente y birthdate válido |
| RF7 | Crear proyectos con nombre único y departamento controlador obligatorio |
| RF8 | Solo Ingenieros o Representantes de Ventas pueden participar en proyectos |
| RF9 | Consultar: empleados por departamento, proyectos por departamento, proyectos de un ingeniero, hijos de un empleado |
| RF10 | Validar restricciones antes de eliminar: departamentos con empleados/proyectos, empleados con hijos |

---

## 6. Restricciones

- No se acepta un único archivo `.py` con todo el sistema
- No se acepta solución puramente procedimental (sin clases ni jerarquía)
- No se permite introducir entidades o relaciones que no estén en el enunciado
- Se exige consistencia entre el modelo de clases y la implementación
- No se admite omitir modularización, principios de POO ni manejo de excepciones

---

## 7. Entregables

1. **Modelo de clases** (UML o equivalente) en PDF o imagen
2. **Código fuente** completo (carpeta con paquetes y módulos)
3. **Documento breve (1–2 páginas)** con:
   - Descripción de la arquitectura (paquetes/módulos)
   - Justificación de herencia y polimorfismo
   - Decisiones relevantes de modelado
