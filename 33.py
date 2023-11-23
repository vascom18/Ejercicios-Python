'''Escribí un programa que permita al usuario ingresar una cantidad de números positivos indefinida (la cantidad que ingresará
 no se conoce y puede cambiar en cada ejecución), finalizando cuando ingresa el número 0 (que no se tendrá en cuenta).
   Una vez terminada la lectura de números, informar cuál fue el mayor de los números ingresados.
 
Ejemplo de ejecución:

Número: 6
Número: 9
Número: 2
Número: 12
Número: 0
Mayor número ingresado: 12'''

mayornum = 0

while True:
    num = int(input('ingrese un numero:'))
    if num == 0:
        break
    if num > mayornum:
        mayornum = num

print(f'el mayor numero ingresado fue: {mayornum}')
