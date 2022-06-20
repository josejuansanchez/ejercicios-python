import random

# Paso 1. Leemos por teclado la opción del usuario
print("0 - Cara")
print("1 - Cruz")
opcion = int(input("Introduce una opción (0 o 1):"))

# Paso 2. Generamos un número aleatorio
moneda = random.randint(0, 1)

# Paso 3. Mostramos el valor de la moneda que ha sacado la máquina
if moneda == 0:
    print("Ha salido CARA")
else:
    print("Ha salido CRUZ")

# Paso 4. Comparamos la opción del usuario con el valor generado
if opcion == moneda:
    print("Enhorabuena, has ganado!!")
else:
    print("Lo siento, has pedido...")