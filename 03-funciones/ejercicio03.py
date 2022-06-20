# Definimos la función saludar
def saludar(nombre, apellido1, apellido2):
    print(f"¡Hola {nombre} {apellido1} {apellido2}!")

#--------------------------------------------------
# Programa Principal
# Utilizamos la función saludar
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

saludar(nombre, apellido1, apellido2)