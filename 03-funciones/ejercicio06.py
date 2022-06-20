# Definimos la función
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

#--------------------------------------------------

# Programa Principal (Main)
base = float(input("Introduce el valor de la base: "))
altura = float(input("Introduce el valor de la altura: "))
area = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo es {area}")