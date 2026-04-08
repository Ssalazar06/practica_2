Este trabajo se desarrolló a partir del enunciado del taller y se organizó con una arquitectura modular para separar responsabilidades. El sistema quedó dividido en cuatro partes: modelos, servicios, consola y utilidades. Con esta separación, la interfaz de usuario en consola no mezcla la lógica de negocio ni el almacenamiento en memoria, y eso hace que el código sea más claro y más fácil de mantener.

En el modelo de clases, la entidad base para las personas es Person. A partir de esta clase se construye Employee, que representa al empleado general. Luego se aplica herencia para los roles especializados: Manager, SalesRepresentative, Engineer y SalesEngineer. Esta jerarquía permite cumplir con el dominio solicitado y reutilizar comportamiento común sin repetir código.

El principio de encapsulamiento se aplicó usando atributos privados y métodos de acceso. De esta forma, los datos internos no se manipulan directamente desde cualquier parte del programa, sino por medio de operaciones controladas en cada clase. Esto ayuda a mantener consistencia en reglas como evitar duplicados y validar relaciones.

También se evidencia polimorfismo en el método can_join_projects. Cada tipo de empleado responde de forma diferente según su rol. Por ejemplo, Manager no participa en proyectos, mientras que Engineer y SalesRepresentative sí pueden hacerlo. Esta decisión permite que la lógica en servicios sea más limpia porque se apoya en el comportamiento de cada objeto.

Para las estructuras de datos se usaron listas y diccionarios. Las listas permiten recorrer colecciones para mostrar información en menús, y los diccionarios permiten búsquedas rápidas por claves como SSN o nombre de proyecto. Esta combinación mejora la legibilidad y mantiene un buen rendimiento para el tamaño esperado del ejercicio.

Las relaciones del dominio también quedaron reflejadas: un empleado pertenece a un departamento, un departamento tiene múltiples empleados y ubicaciones, un departamento controla proyectos, y un empleado puede tener hijos asociados. Además, se incluyeron validaciones de reglas funcionales importantes como unicidad de departamento, unicidad de empleado, unicidad de proyecto, restricción de un manager por departamento y control de eliminación cuando existen dependencias activas.

En conclusión, la implementación mantiene coherencia entre el problema planteado, el diseño orientado a objetos y el código final. Se priorizó una solución simple, funcional y entendible, adecuada para un contexto académico y alineada con los requisitos principales del taller.
