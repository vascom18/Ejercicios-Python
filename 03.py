'''03 - Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado 
de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable
. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
 
Ejemplo de ejecución:

Ingresá un número: 1
Ingresá otro número: 2
Suman: 3
Ingresá un nuevo número: 3
Multiplicación de la suma por el último número: 9

(sin usar funciones)'''

num1=int(input('ingrese un numero entero: '))

num2=int(input('ingrese otro numero entero: '))

resultado_suma = num1 + num2

print('Suman: ' +str(resultado_suma))

num3=int(input('ingrese otro numero entero: '))

print('multiplicacion de la suma por el ultimo numero: ' + str(resultado_suma*num3))

