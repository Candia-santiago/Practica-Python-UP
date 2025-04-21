numSemana = int (input("Ingrese el numero de la semana: "))
gastoTotal = 0
gastoAcumulado = 0

while numSemana < 5:

	gastoSemanal = int (input("**gasto semanal**: "))
	print (f"Total de gasto en la semana {numSemana} fue: {gastoSemanal}")

	gastoAcumulado = gastoAcumulado + gastoSemanal
	print (f"el gasto acumulado entre todas las semanas es: {gastoAcumulado}")
	
	print ("")
	numSemana = int (input("Ingrese el numero de la semana: "))

print ("Llego al final de las semanas")
gastoTotal = gastoTotal + gastoAcumulado
print (f"Su gasto total en las {numSemana} semanas fue: {gastoTotal}")
