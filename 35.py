'''5 - Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo carácter),
 uno por vez. La repetición finalizará cuando se ingrese un string que no tenga longitud 1, o cuando el string ingresado
   corresponda al dígito numérico 0. Al finalizar, mostrar el string completo que se formó con todos los caracteres ingresados
     y qué porcentaje de caracteres del total fueron la letra “a”.
 
Ejemplo de ejecución:

Escribí un carácter: L
Escribí un carácter: 9
Escribí un carácter: a
Escribí un carácter: 4
Escribí un carácter: A
Escribí un carácter: 0
Escribí un carácter: N
Escribí un carácter: a
Escribí un carácter: a
Escribí un carácter: 5
El string completo es: L9a4A0Naa
Porcentaje de letras ‘a’: 33.333333333333336'''

frase = ''
caracteres = 0
letras_a = 0

while True:
    entrada = input('ingrese caracter:')
    if entrada == "0" or len(entrada) > 1:
        print(f"el string completo es: {frase}")
        print(
            f'El porcentaje de letras "a" es de: {(caracteres/letras_a)*10}')
        break
    else:
        caracteres += 1
        frase += entrada
        if entrada == "a":
            letras_a += 1
