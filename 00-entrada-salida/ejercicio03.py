import math

# Paso 1. Leemos por teclado el valor de los dos catetos
cateto1 = float(input("Introduce el valor del cateto 1: "))
cateto2 = float(input("Introduce el valor del cateto 1: "))

# Paso 2. Calculamos la hipotenusa
hipotenusa = math.sqrt((cateto1*cateto1) + (cateto2*cateto2))
#hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
#hipotenusa = math.sqrt(math.pow(cateto1,2) + math.pow(cateto2,2))

# Paso 3. Mostramos el resultado
print(f"El valor de la hipotenusa es {hipotenusa}")