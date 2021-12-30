'''
Escribe un programa que almacene lenguajes de programación en una lista.

El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no"
y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:

¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.

Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. Algo así:
    - JavaScript: no
    - TypeScript: sí
    - Python: sí
    - Dart: no
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

print(json.dumps(respuestas, sort_keys = False, indent = 4))