'''
Escribe un programa que pida al usuario los siguientes datos por consola:
 - Título de la película
 - Director
 - Año
 - País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"
'''

def data_film(): #podemos hacerlo de esta primera manera --> definiendo la variable
    titulo = input('Escriba el título de la película: ')
    pelicula:dict = dict({
        'titulo': titulo
    })
    return pelicula

def data_film2(): #podemos hacerlo de esta primera manera --> NO definiendo la variable
    pelicula:dict = dict({
        'titulo': input('Escriba el título de la película: ')
    })
    return pelicula
primera_pelicula = data_film2()
print(primera_pelicula)