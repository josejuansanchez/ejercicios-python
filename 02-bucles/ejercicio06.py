# Paso 1. Leer por teclado un número comprendido entre 1 y 10
numero = int(input("Introduce un ńumero entre 1 y 10: "))
while numero < 1 or numero > 10:
    print("Error. El número no es válido.")
    numero = int(input("Introduce un ńumero entre 1 y 10: "))

# Paso 2. Mostramos la tabla de multiplicar
for valor in range(1,11,1):
    print(f"{numero}x{valor}={numero*valor}")
