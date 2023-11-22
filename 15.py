'''15 - Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si 
la primera palabra es menor que la segunda o False si no lo es.
 
Ejemplo de ejecución:

Una palabra: complejidad
Otra palabra: algoritmo
False'''

pal1 = input('ingrese la primer palabra:')
pal2 = input('ingrese una segunda palabra: ')

if pal1 < pal2:
    print(True)

else:
    print(False)
