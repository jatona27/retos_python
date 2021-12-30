'''
Escribe un programa que almacene en una lista (Array)
todos los nombres de los alumnos del curso Programación para No Programadores
y los muestre en por pantalla.
'''

def insert_stud_name():
    student = input('Introduzca el nombre del alumno: ')
    return student
list_stud = []
numero_alumnos = 7
for i in range(numero_alumnos):
    list_stud.append(insert_stud_name())
for i in range(len(list_stud)):
    print('Alumno ', i,' : ', list_stud[i])
