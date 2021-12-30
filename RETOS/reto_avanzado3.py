'''
El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:

        - Si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
        - En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
        - Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
        - Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
        - Si la persona es menor de 16 años, no tiene que pagar impuestos

Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas**
durante un año entero (12 meses)
'''

pago_imp = 0
edad = 0
ingresos = 0
pagadores = [
          {'Nombre':'Jaime', 'Ingresos':500, 'Edad':16}, \
          {'Nombre':'Pilar', 'Ingresos':795, 'Edad':24}, \
          {'Nombre':'Pepita', 'Ingresos':900, 'Edad':69}, \
          {'Nombre':'Vicente', 'Ingresos':2900, 'Edad':36}, \
          {'Nombre':'Carlos', 'Ingresos':1500, 'Edad':76}
            ]
def retencion(ingresos):
    if ingresos < 800:
        pago_imp = ingresos*0.1*12
    elif ingresos<2000:
        pago_imp = ingresos*0.3*12
    else:
        pago_imp = ingresos*0.5*12
    return pago_imp

total_imp = 0

for pagador in pagadores: #recorremos la lista de diccionarios
    edad = pagador.get('Edad')
    ingresos = pagador.get('Ingresos')
    #condición para aplicar el descuento según el género:
    if (edad<=16):
        pago_imp = 0
    elif (edad<70):
        pago_imp = retencion(ingresos)
    else:
        pago_imp = 0

    total_imp = total_imp + pago_imp
    print(pagador.get('Nombre') + ' con edad ' + str(edad) + ' e ingresos mensuales de ' + str(ingresos) + ', debe pagar esta cantidad anual de impuestos: ' + str(pago_imp))

print('El impuesto total a pagar por los ' + str(len(pagadores)) + ' pagadores este año es de: ' + str(total_imp) + '€')