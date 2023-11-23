'''34 - Escribí un programa que pregunte al usuario si desea analizar calificaciones de alumnos y,
 sólo si responde “S” comenzará el procesamiento de los datos, hasta que el usuario ingrese algo diferente de “S”.
   Por cada alumno, permitir ingresar su calificación. Si es mayor a 4 el alumno está aprobado. 
   Finalmente, mostrar “Porcentaje de alumnos aprobados: x %” 
   (donde x es el porcentaje de aprobados sobre el total de calificaciones procesadas). 
   También se debe imprimir “Promedio de los aprobados: y” (donde y es la calificación promedio, sólo de los alumnos aprobados).
 
Ejemplo de ejecución:

¿Analizar calificaciones? ‘S’ para ‘sí’: S
Calificación de un alumno: 9
¿Continuar? ‘S’ para ‘sí’: S
Calificación de un alumno: 4
¿Continuar? ‘S’ para ‘sí’: S
Calificación de un alumno: 8
¿Continuar? ‘S’ para ‘sí’: N
Porcentaje de alumnos aprobados: 66.66666666666667 %
Promedio de los aprobados: 8.5

'''
aprobados = 0
suma_aprobados = 0
alumnos = 0
while True:
    opcion = input('Desea analizar calificaciones?: ("s" para si)')
    if opcion != 's':
        print(f'Procentaje de alumnos aprobados:{aprobados/alumnos*100}%')
        print(f'Promedio de los aprobados: {suma_aprobados/alumnos}')
        break
    else:
        calificacion = int(input('Ingrese la calificacion: '))
        alumnos += 1
        if calificacion > 4:
            aprobados += 1
            suma_aprobados += calificacion
