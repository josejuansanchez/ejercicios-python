# Paso 1. Leemos una temperatura por teclado
celsius = float(input('Introduce una temperatura en grados Celsius: '))

# Paso 2. Convertimos de grados Celsius a Farenheit
farenheit = (1.8 * celsius) + 32

# Paso 3. Mostramos el resultado por pantalla
print(f'La temperatura en grados Farenheit es: {farenheit}')