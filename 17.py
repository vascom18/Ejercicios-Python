'''17 - Escribí un programa que, dado un número entero, muestre su valor absoluto. Recordá que, para los números positivos su valor
 absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número
   multiplicado por -1 (el valor absoluto de -52 es 52).
 
Ejemplo de ejecución:

Número: -12
Valor absoluto: 12

'''
num = int(input('igrese un numero:'))

print(f'numero {num}')
if num < 0:

    print(f'valor absoluto: {num*-1}')

else:
    print(f'valor absoluto: {num}')
