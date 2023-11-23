'''37 - Escribí un programa para solicitar al usuario que ingrese números enteros positivos (la cantidad que ingresará no se 
conoce y la decide el usuario). La lectura de números finalizará cuando el usuario ingrese el número -1. Por cada número
 ingresado, mostrar la cantidad de dígitos pares y la cantidad de dígitos impares que tiene. Al finalizar, mostrar cuántos
 números múltiplos de 3 ingresó el usuario.
 
Ejemplo de ejecución:

Número (-1 para terminar el programa): 123
Dígitos pares: 1
Dígitos impares: 2
Número (-1 para terminar el programa): 44
Dígitos pares: 2
Dígitos impares: 0
Número (-1 para terminar el programa): 9
Dígitos pares: 0
Dígitos impares: 1
Número (-1 para terminar el programa): -1
Se ingresaron 2 múltiplos de 3.
'''

mult3 = 0
while True:
    num = input('Ingrese un numero:')
    if num == '-1':
        print(f'se ingresaron {mult3} multiplos de 3')
        break
    pares = 0
    impares = 0
    for i in num:
        if int(i) % 2 == 0:
            pares += 1

        else:
            impares += 1

    if int(num) % 3 == 0:

        mult3 += 1

    print(f'digitos pares: {pares}')
    print(f'digitos impares: {impares}')
