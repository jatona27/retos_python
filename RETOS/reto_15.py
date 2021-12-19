'''
Reto 15:
Escribe una función que reciba una muestra de números en una lista
y devuelva otra lista con sus cuadrados.
'''

def cuadrados(lista_num):
    lista_cuadrados = []
    for i in lista_num:
        lista_cuadrados.append(i**2)
    return lista_cuadrados

lista_num = [3, 4, 5, 6]
lista_cuadrados = cuadrados(lista_num)
print(lista_cuadrados)