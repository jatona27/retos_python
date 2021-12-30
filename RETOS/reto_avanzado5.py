'''
Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la
lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce.
'''

import json

lenguajes = ['JavaScript', 'TypeScript', 'Python', 'Dart']
respuestas = {}

for lenguaje in lenguajes:
    respuesta_correcta = False
    while (not respuesta_correcta):

        respuesta = input('¿Conoces el lenguaje de programación ' + lenguaje + '?: ')
        if respuesta == 'si' or respuesta == 'no':
            respuesta_correcta = True

    respuestas[lenguaje] = respuesta

#print(json.dumps(respuestas, sort_keys = False, indent = 4))

for lenguaje in respuestas:
    respuesta = respuestas[lenguaje]
    if respuesta == 'no':
        print(lenguaje, ': ', respuesta)
