#Escribe un programa que guarde en una variable el siguiente contenido:
#{'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}

pelicula:dict = dict({
        'titulo': 'El Más Allá',
        'aka':'E tu vivrai nel terrore - Laldilà',
        'director':'Lucio Fulci',
        'año': 1981,
        'país': 'Italia'
    })

print(f' - Nombre de la pelicula: ', pelicula.get('titulo'))
print(f' - AKA de la pelicula: ', pelicula.get('aka'))
print(f' - Director de la pelicula: ', pelicula.get('director'))
print(f' - Año de la pelicula: ', pelicula.get('año'))
print(f' - País de la pelicula: ', pelicula.get('país'))
