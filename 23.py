'''23 - Escribí un programa que le solicite al usuario un número entero y muestre todos los números correlativos entre el 
1 y el número ingresado por el usuario.
 
Ejemplo de ejecución:

Ingresá un número: 3
1
2
3
'''

num = int(input('ingrese un numero: '))

for i in range(1, (num+1)):
    print(i)
