class Perro:
    clasificacion = "Cuadrupedo"

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.esta_sentado = False

    def definir_nombre(self, nombre: str) -> None:
        self.__validar_nombre(nombre)
        self.__nombre = nombre

    def __validar_nombre(self, nombre) -> None:
        if nombre == "Carolina":
            raise ValueError("No se puede llamar Carloina a un Perro.")

    def mostrar_nombre(self) -> str:
        return f'Mi nombre es {self.__nombre}'

    def sentarse(self) -> None:
        self.esta_sentado = True

    @staticmethod
    def ladrar() -> None:
        print("Woff wof")
