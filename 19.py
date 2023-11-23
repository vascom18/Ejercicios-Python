'''19 - Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el 
usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
 
Ejemplo de ejecución:

Letra: o
Es vocal'''

letra = input('ingrese una letra: ')
vocales = 'aeiou'

if len(letra) > 1:
    print('no se puede procesar el dato')
else:
    for l in vocales:
        if letra == l:
            print('es vocal')
