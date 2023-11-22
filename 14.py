''' 14 - Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es 
un número par, o False si no lo es.
 
Ejemplo de ejecución:

Ingresá una frase: Era el mejor de los tiempos, era el peor de los tiempos.
True'''
cadena = input(' ingrese una cadena de texto:')

print(f'la cantidad de caracteres de tu frase es {len(cadena)}')

if len(cadena) % 2 == 0:
    print(True)
else:
    print(False)
