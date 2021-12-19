'''
Reto 14:
Escribe una función que use la función del área del círculo para devolver el
volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
'''

import math


def area_circulo(radio):
    area = float(math.pi * radio ** 2)
    return area

radio = float(input('Introduzca la medida en cm del radio del cilindro: '))
altura = float(input('Introduzca la medida en cm de la altura del cilindro: '))
volumen_cilindro = round(area_circulo(radio)*altura, 2)
print(f'El volumen del cilindro con radio {radio} cm y altura {altura} cm es de {volumen_cilindro} cm^3')