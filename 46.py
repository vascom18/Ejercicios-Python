'''46 - -Desarrolle un programa que solicite 10 palabras ingresadas por teclado. El programa debe separar las vocales y las letras 
en dos cadenas primero las vocales seguidas de un guion y
luego las letras. 

Ejemplo de ejecucion: palabra -- aaa-plbr.
'''

vocales = 'aeiou'

for i in range(0, 10):
    voc_pal = ''
    let_pal = ''
    palabra = input('Ingrese un palabra: ')
    for l in palabra:
        vocal = False
        for v in vocales:
            if l == v:
                vocal = True
        if vocal:
            voc_pal += l
        else:
            let_pal += l
    print(f'{palabra} -- {voc_pal} - {let_pal}')
