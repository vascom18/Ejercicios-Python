'''45 - Escribí un programa que permita al usuario ingresar números enteros hasta que ingrese uno cuyo dígito inicial sea el 9 
(el cual no se procesará). Una vez terminada la repetición, mostrar cuántos de los números que el usuario ingresó tienen sólo 
dos divisores (para esto es posible reutilizar parte de la estrategia elaborada en el ejercicio 25).
 
Ejemplo de ejecución:

Número entero: 167
Número entero: 11
Número entero: 821
Número entero: 38
Número entero: 292
Número entero: 3
Número entero: 954
Tienen sólo 2 divisores: 4 números'''
divisores2 = 0
while True:
    num = input('Igrese un numero entero: ')
    if num[0] == '9':
        print(f'Tienen solo 2 divisores: {divisores2} numeros')
    else:
        div = 0
        for i in range(1, int(num)+1):
            if int(num) % i == 0:
                div += 1
        if div == 2:
            divisores2 += 1
