peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura*altura)

print(f"El valor del IMC es {imc}")