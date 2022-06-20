# Definimos la función
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

#--------------------------------------------------

# Programa Principal (Main)
base = float(input("Introduce el valor de la base: "))
altura = float(input("Introduce el valor de la altura: "))
area = calcular_area_triangulo(base, altura)
print(f"El área del triángulo es {area}")