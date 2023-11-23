'''21 - Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña
 es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no 
 coinciden, mostrar “Acceso denegado”.
 
Ejemplo de ejecución:

Nombre de usuario: gwen
Contraseña: excalibur
Acceso denegado'''

user = input('ingrese su usuario: ')

passw = input('ingrese una contrasenia: ')

if user == 'Gwenevere' and passw == 'excalibur':
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')
