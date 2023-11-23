'''escribí un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando
 el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
   Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el monto total de 1000, se le 
   debe aplicar un 10% de descuento.
 
Ejemplo de ejecución:

Monto de una venta: $ 100
Monto de una venta: $ 300
Monto de una venta:$ -1
Monto no válido.
Monto de una venta: $ 2000
Monto de una venta: $ 0
Monto total a pagar: $ 2160.0'''
suma = 0

while True:
    monto = int(input('Ingrese el monto de la venta: '))
    if monto < 0:
        print('monto invalido')

    else:
        suma += monto
        if monto == 0:
            if suma > 1000:
                print(f'Monto total a pagar: {suma*0.9}')
                break
            else:
                print(f'Monto total a pagar: {suma}')
                break
