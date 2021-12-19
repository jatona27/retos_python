'''
Reto 17:
Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

Realiza las siguientes operaciones
    Encontrar los elementos de 3 a 5
    Encontrar los 6 primeros elementos
    Muestra la tupla desde el 5 elemento hasta el final
    Muestra toda la tupla haciendo uso de [:]
    Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
    Devuelve la tupla con un salto cada 4 elementos
    Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
'''

tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

#Encontrar los elementos de 3 a 5
print(tupla[3:6])

#Encontrar los 6 primeros elementos
print(tupla[0:6])

#Muestra la tupla desde el 5 elemento hasta el final
print(tupla[4:])

#Muestra toda la tupla haciendo uso de [:]
print(tupla[:])

#Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
for i in range(1,9,2):
  print(tupla[i])

#Devuelve la tupla con un salto cada 4 elementos
for i in range(0,len(tupla),4):
  print(tupla[i])

#Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
for i in range(9,1,-1):
  print(tupla[i])