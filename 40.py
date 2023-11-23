''' 40 - Escribí un programa que permita al usuario ingresar títulos de libros por teclado,
 finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 
 que contenga sólo una barra “/” se considera que termina una línea. Por cada línea completa, informar cuántos dígitos
numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente,
 informar cuántas líneas completas se ingresaron.
 
Ejemplo de ejecución:

Cadena: Don Quijote de La Mancha
Cadena: Los 3 mosqueteros
Cadena: Historia de 2 ciudades
Cadena: /
Aparecen 2 dígitos en la línea
Cadena: 20000 leguas de viaje submarino
Cadena: El señor de los anillos
Cadena: Alicia en el país de las maravillas
Cadena: 1984
Cadena: El hobbit
Cadena: /
Aparecen 9 dígitos en la línea
Cadena: Divina comedia
Cadena: Drácula
Cadena: /
Aparecen 0 dígitos en la línea
Cadena: 20 años después
Cadena: Los viajes de Gulliver
Cadena: *
Se leyeron 3 líneas completas
'''
bandera = ''
while bandera == '':
    contador_digitos = 0
    lineas = 0
    while True:
        cadena = input('ingrese titulo de libro')
        if cadena == '/':
            lineas += 1
            print(f'aparecen {contador_digitos} digitos en la linea')
            contador_digitos = 0
        elif cadena == '*':
            print(f'se leyeron {lineas} lineas completas')
            bandera = 'no'
            break
        else:
            for i in cadena:
                if i.isdigit():
                    contador_digitos += 1
