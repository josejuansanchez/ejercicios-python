# Paso 1. Leemos la nota por teclado
nota = float(input('Introduce una nota entre 0 y 10: '))

# Paso 2. Comprobamos la nota
if nota >= 0 and nota < 5:
    print("Insuficiente")
elif nota >= 5 and nota < 6:
    print("Suficiente")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota < 10:
    print("Sobresaliente")
else:
    print("La nota no es válida")