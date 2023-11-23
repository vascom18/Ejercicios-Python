'''36 - Escribí un programa que, dado un número entero por el usuario (guardado como int), muestre la suma de todos sus dígitos.
 Recordá que vas a necesitar obtener cada uno de los dígitos por separado para poder sumarlos entre sí.
 
Ejemplo de ejecución:

Escribí un número: 7124
Suma de los dígitos: 14'''


num = int(input('Ingrese un numero: '))
suma = 0

for i in str(num):
    suma += int(i)
print(suma)
