# Inicializamos la variable respuesta
respuesta = "s"

while respuesta == "s" or respuesta == "S":
#while respuesta.upper() == "S":
#while respuesta.lower() == "s":
        
    # Paso 1. Leer por teclado un número comprendido entre 1 y 10
    numero = int(input("Introduce un ńumero entre 1 y 10: "))
    while numero < 1 or numero > 10:
        print("Error. El número no es válido.")
        numero = int(input("Introduce un ńumero entre 1 y 10: "))

    # Paso 2. Mostramos la tabla de multiplicar
    for valor in range(1,11,1):
        print(f"{numero}x{valor}={numero*valor}")

    # Paso 3. Preguntar al usuario si desea volver a ejecutar el código
    respuesta = input("¿Desea volver a ejecutar el programa (s/n)? ")