'''Escribí una función que reciba un string y retorne True si es un palíndromo (esto es, si se lee igual de izquierda a derecha 
o de derecha a izquierda), False en caso contrario. Utilizar esta función en un programa que permita al usuario ingresar palabras
 hasta que ingrese la palabra “fin” (suponer que todas las palabras son en minúsculas o todas en mayúsculas, de forma consistente).
  Al finalizar, mostrar la cantidad de palíndromos ingresados.
 
Ejemplo de ejecución:

Cadena: abba
Cadena: m
Cadena: luz
Cadena: reconocer
Cadena: golondrina
Cadena: fin
Cantidad de palíndromos: 3'''


def esPalindromo(txt):
    inv = ''
    for i in txt:
        inv = i+inv
    if inv == txt:
        return True
    else:
        return False


palindromos = 0
while True:
    palabra = input('Por favor ingrese una palabra: ')
    if palabra. lower() == 'fin':
        print(f'Cantidad de palindromos: {palindromos}')
        break
    else:
        if esPalindromo(palabra):
            palindromos += 1
