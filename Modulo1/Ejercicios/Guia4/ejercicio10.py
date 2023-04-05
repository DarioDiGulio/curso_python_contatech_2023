number = int(input("Ingresá un número entero positivo mayor que 2: "))
i = 2
while number % i != 0:
    i += 1

if i == number:
    print(f"{number} es primo")
else:
    print(f"{number} no es primo")
