#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('Introduce tu edad: '))
while edad < 18:
    if edad > 18:
        print('Usted es mayor de edad')
        break
    else:
        print('Usted es menor de edad')
        edad = int(input('Introduce tu edad: '))