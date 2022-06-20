import random

# Paso 1. Leemos por teclado la opción seleccionada por el usuario
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
jugada_usuario = int(input("Seleccione una opción (1, 2 o 3): "))

# Paso 2. Generamos un número entero aleatorio entre 1 y 3
jugada_ordenador = random.randint(1, 3)

# Paso 3. Mostramos la jugada del ordenador
if jugada_ordenador == 1:
    print("El ordenador ha sacado: PIEDRA")
elif jugada_ordenador == 2:
    print("El ordenador ha sacado: PAPEL")
else:
    print("El ordenador ha sacado: TIJERA")

# Paso 4. Comparamos la jugada del usuario con la del ordenador
if jugada_usuario == jugada_ordenador:
    print("Hay un EMPATE")
elif jugada_usuario == 1 and jugada_ordenador == 3:
    print("Gana el USUARIO")
elif jugada_usuario == 2 and jugada_ordenador == 1:
    print("Gana el USUARIO")
elif jugada_usuario == 3 and jugada_ordenador == 2:
    print("Gana el USUARIO")
else:
    print("Gana el ORDENADOR")

    