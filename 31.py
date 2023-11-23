''' Escribí un programa que, dada una frase por el usuario, la muestre invertida, sin utilizar una rebanada con paso negativo.
 
Ejemplo de ejecución:

Frase: Sabía quién era esta mañana, pero he cambiado varias veces desde entonces
secnotne edsed secev sairav odaibmac eh orep ,anañam atse are néiuq aíbaS'''


frase = input('por favor escriba una frase: ')

fraseinv = ''

for i in frase:
    fraseinv = i+fraseinv

print(fraseinv)
