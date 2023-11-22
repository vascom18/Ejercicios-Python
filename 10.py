"""10 - Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese
 número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto 
 más de 3 shows.
 
Ejemplo de ejecución:

Shows vistos en el último año: 3
False"""


n_shows = int(
    input('por favor ingrese la cantidad de shows que viste este anio:'))

print(f'Shows vistos este anio:{n_shows}')

print(n_shows > 3)
