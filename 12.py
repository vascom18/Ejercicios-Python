"""12 - Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo
 de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.

 
Ejemplo de ejecución:

Número entero: 7254
True  """

num = int(input('por favor ingrese un numero:'))
print(f'el numero entero : {num}')
if num % 2 == 0:
    print(True)
else:
    print(False)
