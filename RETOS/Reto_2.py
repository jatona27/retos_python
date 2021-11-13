#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
print('Introduce el primer numero: ')
desde = int(input())
print('Introduce el ultimo numero: ')
hasta = int(input())
while desde <= hasta:
    if desde % 2 != 0:
        print(desde)
    desde += 1