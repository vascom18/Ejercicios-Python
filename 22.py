'''escribí un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe 
ser divisible por 100, excepto que también sea divisible por 400.
 
Ejemplo de ejecución:

Año: 2020
Bisiesto'''

anio = int(input('ingrese un anio:'))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print('Es bisiesto')
    else:
        print('Es bisiesto')
