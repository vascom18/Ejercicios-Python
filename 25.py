'''25 - Escribí un programa que, dado un número por el usuario, muestre todos sus divisores positivos. Recordá que un divisor es aquel que divide al número de forma exacta (con resto 0).
 
Ejemplo de ejecución:

Número: 14
Divisores:
1
2
7
14

'''

num = int(input('ingrese un numero: '))
print(f'Numero: {num}')

for i in range(1, num+1):
    if num % i == 0:
        print(i)
