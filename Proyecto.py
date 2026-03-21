from datetime import date

class Proyecto:
    __id_proyecto:str
    __nombre_proyecto:str
    __fecha_inicio_proyecto:date

    def __init__(self, id_proyecto:str, nombre_proyecto:str, fecha_inicio_proyecto:date):
        self.__id_proyecto = id_proyecto
        self.__nombre_proyecto = nombre_proyecto
        self.__fecha_inicio_proyecto = fecha_inicio_proyecto