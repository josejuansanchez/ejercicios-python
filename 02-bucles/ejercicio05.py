numero = float(input("Introduce un número entre 1 y 10: "))
while numero < 1 or numero > 10:
    print("Error. El número no es correcto")
    numero = float(input("Introduce un número entre 1 y 10: "))