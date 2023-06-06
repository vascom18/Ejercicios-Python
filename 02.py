'''02 - Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el
  programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá 
  guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.
 
Ejemplo de ejecución:

Primer número: 14.2
Segundo número: 19
El resultado de la suma es 33.2

(no es necesario usar funciones)'''


num1= float(input('ingrese un numero decimal: '))

num2= int(input('Ingrese un numero entero: '))

print('El resultado de la suma es: ' + str(num1+num2))


