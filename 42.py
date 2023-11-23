'''Escribí una función llamada sumatoriaDigitos que reciba como parámetro un número y retorne la suma de todos sus dígitos,
 reutilizando la estrategia utilizada en el ejercicio 36. Finalmente, escribir un algoritmo que solicite al usuario ingresar
  varios números hasta que ingrese el número 100, con el cual cortará la repetición. Por cada número, mostrar la suma de sus
   dígitos, para lo cual se llamará a la función sumatoriaDigitos.
 
Ejemplo de ejecución:

Escribí un número: 7124
Suma de los dígitos: 14
Escribí un número: 20
Suma de los dígitos: 2
Escribí un número: 916
Suma de los dígitos: 16
Escribí un número: 100'''


def sumatoriaDigitos(numero):

    suma = 0
    for i in str(numero):
        suma += int(i)
    return suma


while True:
    sumatoria = 0
    num = int(input('Ingrese un numero: '))
    if num == 100:
        break
    else:
        sumatoria += sumatoriaDigitos(num)
        print(f'Sumatoria de digitos: {sumatoria}')
        sumatoria = 0
