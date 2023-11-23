'''Escribí un programa que permita al usuario ingresar números enteros. La repetición terminará cuando el usuario ingrese un 
número para el cual la suma de sus dígitos sea mayor que 1000 ó múltiplo de 5. Finalmente, mostrar cuántos números impares ingresó
 el usuario antes de cortar la repetición. Reutilizar las funciones esPar y sumatoriaDigitos implementadas en los ejercicios 
 anteriores.
 
Ejemplo de ejecución:

Escribí un número: 16
Escribí un número: 922
Escribí un número: 1513
Escribí un número: 481
Escribí un número: 90
Cantidad de impares: 2'''


def sumatoriaDigitos(numero):

    suma = 0
    for i in str(numero):
        suma += int(i)
    return suma


def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


impares = 0
while True:
    num = int(input('ingrese un numero entero: '))
    if sumatoriaDigitos(num) > 1000 or sumatoriaDigitos(num) % 5 == 0:
        print(f'Cantidad de impares: {impares}')
        break
    else:
        if not esPar(num):
            impares += 1
