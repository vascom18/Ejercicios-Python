'''26 - Escribí un programa que, dada una frase por el usuario, muestre la cantidad total de vocales (tanto mayúsculas como minúsculas)
 que contiene.
 
Ejemplo de ejecución:

Frase: Verde que te quiero verde
Vocales: 11'''

frase = input('por favor escriba una frase: ')
print(f'frase: {frase}')

contador = 0

vocales = ['a', 'e', 'i', 'o', 'u']

for v in frase:

    for i in vocales:

        if i == v:
            contador += 1

print(f'vocales: {contador}')
