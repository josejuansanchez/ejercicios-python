import math

# Definimos la función
def calcular_area_circulo(radio):
    area = math.pi * radio * radio  
    return area

#-------------------------------------------------------
# Programa Principal
radio = float(input("Introduce el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo es {area}")