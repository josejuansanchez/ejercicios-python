import areas
import os

# Definición de funciones
def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def principal():
    opcion = 1
    while opcion != 4:
        os.system("clear")
        mostrar_menu()

        opcion = int(input("Introduce una opción (1-4): "))
        while opcion < 1 or opcion > 4:
            print("Error. La opción no es válida")
            opcion = int(input("Introduce una opción (1-4): "))

        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()

        if opcion != 4:
            input("\nPulse una tecla para continuar...")

def opcion1():
    print("\nOpción 1")
    radio = float(input("Introduce el radio del círculo: "))
    area = areas.calcular_area_circulo(radio)
    print(f"El área del círculo es {area}")    

def opcion2():
    print("\nOpción 2")
    base = float(input("Introduce el valor de la base: "))
    altura = float(input("Introduce el valor de la altura: "))
    area = areas.calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es {area}")

def opcion3():
    print("\nOpción 3")
    base = float(input("Introduce el valor de la base: "))
    altura = float(input("Introduce el valor de la altura: "))
    area = areas.calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es {area}")

#--------------------------------------------
# Programa Principal (Main)

principal()