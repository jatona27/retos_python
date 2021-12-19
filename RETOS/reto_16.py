'''
Reto 16:
Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
'''
from datetime import datetime

fecha_int1 = datetime.strptime(input('Introduzca fecha inicial: '),'%d/%m/%Y')
fecha_int2 = datetime.strptime(input('Introduzca fecha final: '),'%d/%m/%Y')

result = fecha_int2 - fecha_int1

print(result)