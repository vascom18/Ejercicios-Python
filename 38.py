'''38 - Escribí un programa que solicite al usuario una cadena de caracteres (que puede contener letras, números o símbolos).
 Analizar la cadena para mostrar: cuántas letras del abecedario (minúsculas y mayúsculas) contiene, cuántos símbolos
   (caracteres que no son ni letras ni números), cuántos dígitos numéricos y, de los dígitos, cuántos son múltiplos de 4.
 
Ejemplo de ejecución:

Cadena de caracteres: 1984 (novela de George Orwell)
Cantidad de letras: 20
Cantidad de dígitos numéricos: 4
Cantidad de símbolos: 6
Cantidad de múltiplos de 4: 2'''

letras = 0
digitos = 0
mul4 = 0
simbolos = 0

frase = input('ingreses una frase:')

for i in frase:
    if i.isalpha():
        letras += 1
    elif i.isdigit():
        digitos += 1
        if int(i) % 4 == 0:
            mul4 += 1
    else:
        simbolos += 1
print(f'Canttidad de letras: {letras}')
print(f'Canttidad de digitos: {digitos}')
print(f'Canttidad de sibolos: {simbolos}')
print(f'Canttidad de multiplos de 4: {mul4}')
