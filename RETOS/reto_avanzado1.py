'''
Una tienda vende Discos de música. Con la idea de vender un stock almacenado durante meses,
se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.

Cada disco (usa un diccionario para esto) tendrá:
    - Nombre
    - Artista
    - Año
    - Precio
    - Género (solo pueden ser de los siguientes)
        - Pop
        - Electro
        - Reggaeton
        - Rock
        - Metal
        - Death Metal
        - Black Metal

Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir
el disco a comprar.

Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra
(puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.
'''

import json

#Genero una lista de diccionarios ("dicos") con los detalles de cada disco:
discos = [{'Nombre':'Back in Black', 'Artista':'AC/DC', 'Año':'1980', 'Precio':25, 'Genero':'Rock'}, \
          {'Nombre':'YHLQMDLG', 'Artista':'Bad Bunny', 'Año':'2020', 'Precio':15, 'Genero':'Reggaeton'}, \
          {'Nombre':'Nothing Was The Same', 'Artista':'Drake', 'Año':'2013', 'Precio':30, 'Genero':'Pop'}, \
          {'Nombre':'Random Access Memories', 'Artista':'Daft Punk', 'Año':'2013', 'Precio':20, 'Genero':'Electro'}
          ]
#Genero unas variables para seguir o no con la compra --> comprar:
comprar = '1'
#Genero una lista para que más tarde sume los importes:
carrito = []
#Comenzamos con el loop para que vaya rellenando el carrito:
while (comprar == '1'): #tener cuidado porque cuando el usuario mete el 1 o el 0 es un string por tanto cuando lo ponemos en == debe estar entre ''
    print(json.dumps(discos, sort_keys = False, indent = 4)) #Muestro los diccionarios
    respuesta = input('Introduzca el nombre del disco: ') #Pido la entrada
    carrito.append(list(filter(lambda item: item['Nombre'] == respuesta, discos)))
    comprar = input('Si quiere seguir comprando pulse 1, si quiere finalizar su compra pulse 0: ')

importe = 0 #inicializamos la variable
for disco in carrito: #recorremos la lista de diccionarios
    precio = int(disco[0].get('Precio'))
    genero = disco[0].get('Genero')
    #condición para aplicar el descuento según el género:
    if (genero == 'Black Metal' or genero == 'Electro'):
        descuento = 0.3
    else:
        descuento = 0

    #Generamos el ticket:
    nombre_disco = disco[0].get('Nombre')
    importe = importe + precio*(1-descuento)
    print(nombre_disco,'- con precio: ', precio,' y descuento: ', descuento)

print('Importe total: ', importe)

