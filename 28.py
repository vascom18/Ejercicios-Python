'''Escribí un programa que, dado un número entero positivo, calcule y muestre su factorial. El factorial de un número se obtiene 
multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
 
Ejemplo de ejecución:

Número: 7
Factorial: 5040'''

num = int(input('ingrese un numero: '))

print(f'Numero:{num}')

if num == 0:
    print('Factorial: 1')
else:
    for i in range(1, num):

        num *= i
    print(f'Factorial: {num}')
