'''Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y 
le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

 
Ejemplo de ejecución:

Ingresá una temperatura expresada en Farenheit: 75
23.88888888888889'''


temp= float(input('ingrese temperatura en grados fahrenheit:'))

cent=(5/9)*(temp-32)

print('la temperatura en grados centigrados es: '+ str(cent) )

 
                    