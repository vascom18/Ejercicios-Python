'''Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros
 de combustible que consumió durante ese recorrido. Mostrar los kilometros que podemos hacer con un litro de compbustible.
 
Ejemplo de ejecución:

Kilómetros recorridos: 260
Litros de combustible gastados: 12.5
kilometros por litro: 20.8'''


km = int(input('kilometros recorridos: '))
litros=float(input('litros gastados: '))

print('kilometros por litro: '+ str(km/litros) )