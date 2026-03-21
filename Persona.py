from datetime import date

class Persona:
    __id_persona: str
    __p_nombre: str
    __s_nombre: str
    __p_apellido: str
    __s_apellido: str
    __fecha_nacimiento: date

    def __init__(self, id_persona:str, p_nombre:str, s_nombre:str, p_apellido:str, s_apellido:str, fecha_nacimiento:date ):
        self.__id_persona = id_persona
        self.__p_nombre = p_nombre
        self.__s_nombre = s_nombre
        self.__p_apellido = p_apellido
        self.__s_apellido = s_apellido
        self.__fecha_nacimiento = fecha_nacimiento

class Empleado(Persona):
    __ssn:str
    __salario:float

    def __init__(self, ssn:str, salario:float, id_person:str, p_nombre:str, s_nombre:str, p_apellido:str, s_apellido:str, fecha_nacimiento:date):
        super().__init__(id_person, p_nombre, s_nombre, p_apellido, s_apellido, fecha_nacimiento)
        self.__ssn = ssn
        self.__salario = salario

