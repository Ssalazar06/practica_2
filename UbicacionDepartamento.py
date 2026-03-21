class UbicacionDepartamento:
    __id_ubicacion:str
    __direccion:str

    def __init__(self, id_ubicacion:str, direccion:str):
        self.__id_ubicacion = id_ubicacion
        self.__direccion = direccion