'''30 - Escribí un programa que permita al usuario ingresar una frase y luego un carácter (string de longitud 1) y 
luego muestre la frase ingresada, pero con todas las ocurrencias del carácter indicado por el usuario reemplazadas por “*”.
 
Ejemplo de ejecución:

Frase: Aquí me pongo a cantar al compás de la vigüela_
Carácter: o
Aquí me p*ng* a cantar al c*mpás de la vigüela'''


frase = input('ingrese una frase: ')
caracter = input('ingrese caracter: ')
frase = frase.replace(caracter, '*')

print(frase)
