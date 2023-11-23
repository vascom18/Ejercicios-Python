'''29 - Escribí un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos.
 Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos. No olvides que no es posible dividir
   por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
 
Ejemplo de ejecución:

Número: 15
Número: -12
Número: 5
Número: 10
Número: -3
Número: 9
Sumatoria de los negativos: -15
Promedio de los positivos: 9.75
'''

num1 = int(input('ingrese un numero positivo o negativo: '))
num2 = int(input('ingrese un numero positivo o negativo: '))
num3 = int(input('ingrese un numero positivo o negativo: '))
num4 = int(input('ingrese un numero positivo o negativo: '))
num5 = int(input('ingrese un numero positivo o negativo: '))
num6 = int(input('ingrese un numero positivo o negativo: '))

sumaneg = 0
sumapos = 0
cantidad_pos = 0

lista = list((num1, num2, num3, num4, num5, num6))

for i in lista:
    if i < 0:
        sumaneg += i
    else:
        cantidad_pos += 1
        sumapos += i

print(f'la sumatoria de los negativos es {sumaneg}')

if sumapos == 0:
    print('el promedio de la suma es 0')
else:
    print(f'el promedio de la suma es {sumapos/cantidad_pos}')
