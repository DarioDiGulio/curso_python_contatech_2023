# Pedir al usuario su nombre y mostrarlo por pantalla en negrita en cualquier color

user_name = input('Ingresá tu nombre: \n')

print('\033[1m' + user_name + '\033[0m')
