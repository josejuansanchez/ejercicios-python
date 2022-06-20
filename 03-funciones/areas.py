import math

def calcular_area_circulo(radio):
    area = math.pi * radio * radio  
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area
