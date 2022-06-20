import random

# Paso 1. Generamos un número aleatorio entre 0 y 1
numero = random.randint(0, 1)

# Paso 2. Comprobamos si ha salido cara o cruz
if numero == 0:
    print("CARA")
else:
    print("CRUZ")
