'''
El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal),
hasta que el usuario decida terminar ("Introducir otro elemento al carrito (Si / No)".

Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la
compra y el coste total.
'''

cesta = {}
continuar = True
while continuar:
    articulo = input('¿Qué artículo desea comprar?: ')
    precio = float(input('Introduzca el precio de ' + articulo + ': '))
    cesta[articulo] = precio
    continuar = input('¿Quiere continuar comprando? (SI/NO): ') == "SI"
importe = 0

print('Artículos en carrito: ')
for item, precio in cesta.items():
    print(item, '\t', precio)
    importe += precio
print('Importe total: ', importe)