'''
Reto 18:
Crea una función que sea capaz de eliminar un caracter concreto de una cadena de texto.
La función debe tener la siguiente forma:

def eliminar(str, n):
    TODO: Esto debes completarlo
    Pista, haz uso de [start:end:step]

De modo que:
print(eliminar('Madrid', 0)) #adrid
print(eliminar('Madrid', 3)) #Madid
print(eliminar('Madrid', 5)) #Madri
'''

def eliminar(cadena, n):
    if n == 0:
        nueva_cadena = cadena[1:len(cadena)]
    elif n == len(cadena):
        nueva_cadena = cadena[0:len(cadena)-1]
    else:
        nueva_cadena = cadena[0:n] + cadena[n+1:len(cadena)]
    return nueva_cadena

print(eliminar('Madrid', 0))
print(eliminar('Madrid', 3))
print(eliminar('Madrid', 5))