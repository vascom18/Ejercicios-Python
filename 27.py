'''27 -  Escribí un programa que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los 
números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia:

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
 
Ejemplo de ejecución:

0
1
1
2
3
5
8
13
21
34'''

a = 0
b = 1
print(a)
print(b)

for i in range(8):
    a, b = b, a+b
    print(b)
