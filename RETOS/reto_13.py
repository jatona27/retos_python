'''
Escribe una función que calcule el área de un triángulo, recibiendo la altura
y la base como parámetros y otra función que calcule el área de un círculo
recibiendo el radio del mismo.
'''
import math
def area_triangulo(base, altura):
    area = float((base * altura)/2)
    return area

def area_circulo(radio):
    area = float(math.pi * radio**2)
    return area

base = float(input('Introduzca la medida de la base del triángulo: '))
altura = float(input('Introduzca la medida de la altura del triángulo: '))
area_t = area_triangulo(base, altura)
print(f'El área del triángulo con base {base} cm y altura {altura} cm es de {area_t} cm^2')

radio = (input('Introduzca la medida del radio del círculo: '))
area_c = area_circulo(float(radio))
print(f'El área del círculo con radio {radio} cm es de {area_c} cm^2')
