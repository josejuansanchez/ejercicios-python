# Paso 1. Leemos un número entero por teclado
numero = int(input("Introduce un número: "))

# Paso 2. Comprobamos si el número es par o impar 
if numero % 2 == 0:
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")