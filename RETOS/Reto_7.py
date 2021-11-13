'''Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto
introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en
cuenta mayúsculas y minúsculas.'''

true_psswd = 'p2swd0K'
psswd = input('Introduce contraseña: ')
if true_psswd == psswd:
    print('¡Contraseña correcta!')
else:
    input('Contraseña incorrecta. Pruebe de nuevo: ')
