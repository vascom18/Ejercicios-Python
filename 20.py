'''20 - Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
 
Ejemplo de ejecución:

Primer número: 20
Segundo número: 30
Tercer número: 10
Menor: 10'''

num1 = int(input('por favor ingrese un numero: '))
num2 = int(input('por favor otro un numero: '))
num3 = int(input('por favor otro un numero: '))

print(f'primer numero: {num1}')
print(f'segundo numero: {num2}')
print(f'tercer numero: {num3}')

if num1 < num2 and num1 < num3:
    print(f'el menos de los numeros es {num1}')
else:
    if num2 < num3:
        print(f'el menos de los numeros es {num2}')
    else:
        print(f'el menor de los numeros es {num3}')
