# Paso 1. Importamos el módulo de funciones matemáticas
import math

# Paso 2. Leemos el valor del radio por teclado
radio = float(input('Introduce el valor del radio: '))

# Paso 3. Calculamos el área
area = math.pi * radio * radio
#area = math.pi * (radio**2)
#area = math.pi * math.pow(radio, 2)

# Paso 4. Mostramos el resultado
print(f'El área es {area}')

