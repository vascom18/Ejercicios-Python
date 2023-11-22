'''11 - Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan 
el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo 
int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA. No se puede usar la libreria DATATIME
 
Ejemplo de ejecución:

Fecha en formato DDMMAAAA: 16112017
16 / 11 / 2017'''


fecha = int(input('Por favor ingrese una fecha en formato ddmmaaaa:'))

print(f'Fecha en formato DDMMAAA {fecha} ')

# problemas para solucionear este ejecicio: python no permite un int que inicia en 0, lo toma por numero octal, o lo pasamos como string y despues a int, o float, pero int no se podria
