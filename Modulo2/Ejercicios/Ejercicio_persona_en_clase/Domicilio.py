class Domicilio:

    def __int__(self):
        self.__calle = ''
        self.__numero = ''
        self.__ciudad = ''

    def obtener_calle(self) -> str:
        return self.__calle

    def obtener_numero(self) -> str:
        return self.__numero

    def obtener_ciudad(self) -> str:
        return self.__ciudad

    def modificar_calle(self, calle: str) -> None:
        self.__calle = calle

    def modificar_numero(self, numero: str) -> None:
        self.__numero = numero

    def modificar_ciudad(self, ciudad: str) -> None:
        self.__ciudad = ciudad

    def obtener_domicilio_completo(self):
        return f'{self.__calle} {self.__numero}, {self.__ciudad}'
