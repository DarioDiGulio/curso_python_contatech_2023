from Modulo2.Ejercicios.Ejercicio_persona_en_clase.Domicilio import Domicilio
from Modulo2.Ejercicios.Ejercicio_persona_en_clase.Persona import Persona


def main():
    domicilio = Domicilio()
    domicilio.modificar_calle('Rivadavia')
    domicilio.modificar_numero('543')
    domicilio.modificar_ciudad('Ciudad de Buenos Aires')
    persona = Persona()
    persona.modificar_nombre('Fulano')
    persona.modificar_apellido('Gomez')
    persona.modificar_domicilio(domicilio)
    otra_persona = Persona()
    otra_persona.modificar_nombre('Fulana')
    otra_persona.modificar_apellido('Ramirez')
    domicilio.modificar_calle('Hidalgo')
    otra_persona.modificar_domicilio(domicilio)
    print(persona.obtener_nombre_completo())
    print(persona.mostrar_domicilio())
    print(otra_persona.obtener_nombre_completo())
    print(otra_persona.mostrar_domicilio())


if __name__ == '__main__':
    main()
