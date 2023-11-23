'''41 - Escribí una función llamada esPar que reciba como parámetro un número y retorne True si el número es par ó False si es impar.
 Utilizar esta función en un programa que solicite al usuario el ingreso de 10 números y que luego muestre, por separado, la suma
  de todos los pares y la suma de todos los impares.
 
Ejemplo de ejecución:

Número: 620
Número: 12993
Número: 230
Número: 7
Número: 18
Número: 9234
Número: 38
Número: 567
Número: 8146
Número: 32
Suma de los pares: 18318
Suma de los impares: 13567
'''
pares = 0
impares = 0


def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


for i in range(0, 10):
    num = int(input('Ingrese un numero: '))
    if esPar(num):
        pares += num
    else:
        impares += num

print(f'Suma de los pares: {pares}')
print(f'Suma de los impares: {impares}')
