'''Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
 
Ejemplo de ejecución:

Primer número: 8.5
Segundo número: 10
Tercer número: 5.5
El promedio de los tres es 8.0'''

num1= int(input('ingrese un numero: '))

num2= int(input('ingrese otro numero: '))

num3= int(input('ingrese otro numero: '))

promedio= (num1+num2+num3)/3

print('el promedio de los tres es: '+ str(promedio))

print('el promedio de los tres es :'+ str(((num1+num2+num3)/3)))