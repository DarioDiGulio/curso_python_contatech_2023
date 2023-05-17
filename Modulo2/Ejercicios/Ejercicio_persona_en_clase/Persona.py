from Modulo2.Ejercicios.Ejercicio_persona_en_clase.Domicilio import Domicilio


class Persona:
    __domicilio: Domicilio

    def __init__(self):
        self.__nombre = ''
        self.__apellido = ''

    def modificar_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def modificar_apellido(self, apellido: str) -> None:
        self.__apellido = apellido

    def modificar_domicilio(self, domicilio: Domicilio) -> None:
        self.__domicilio = domicilio

    def obtener_nombre_completo(self) -> str:
        return f'{self.__nombre} {self.__apellido}'

    def mostrar_domicilio(self) -> None:
        print(self.__domicilio.obtener_domicilio_completo())
