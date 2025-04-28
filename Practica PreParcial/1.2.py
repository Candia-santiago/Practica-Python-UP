vueltasCiclo = 4

recaudadoA = 0
recaudadoB = 0
recaudadoC = 0

cantAbono1 = 0 
cantAbono2 = 0
cantAbono3 = 0

llamadasMas5 = 0

for i in range (1, vueltasCiclo + 1):
	nom = input ("Ingrese su nombre: ")
	while nom == "":
		nom = input ("ERROR, Ingrese su nombre: ")

	tiempoLlamada = int (input("Ingese el tiempo en Llamada: "))
	while tiempoLlamada < 0:
		tiempoLlamada = int (input("ERROR, Ingese el tiempo en Llamada: "))

	tipoAbono = input ("Ingrese el tipo de Abono: (A/B/C): ")
	while tipoAbono != "A" and tipoAbono != "B" and tipoAbono != "C" :
		tipoAbono = input ("ERROR, Ingrese el tipo de Abono: (A/B/C): ")

	if tipoAbono == "A":
		cantAbono1 += 1
		print ("abono A: ", cantAbono1)
		recaudadoA = tiempoLlamada * 2

	elif tipoAbono == "B":
		cantAbono2 += 1
		print ("abono B: ", cantAbono2)

		if tiempoLlamada <= 5:
			recaudadoB = tiempoLlamada * 2
		else:
			tiempoRestante = tiempoLlamada - 5
			tiempoRestante *=  1.5
			recaudadoB = tiempoRestante + 10
			#print (f"el valor de la llamada pasados los 5 minutos es: {tiempoRestante} , para la reaudacion tot hay que sumarle 10. {tiempoRestante + 10}")
	else:
		cantAbono3 +=1
		print ("Abono C: ", cantAbono3)

		if tiempoLlamada <= 10:
			recaudadoC = tiempoLlamada * 1
			print (recaudadoC)
		else:
			recaudadoC == 10

	if tiempoLlamada > 5:
		llamadasMas5 += 1


print ("------Resultados-------")

totRecaudado = recaudadoA + recaudadoB + recaudadoC
print ("El total recaudado de la empresa es: ", totRecaudado)
print ("")
if cantAbono1 > 0:
	print ("Cant Clientes Abono A: ", cantAbono1)
else:
	print ("No se registraron clientes con abona A")
print ("")
if cantAbono2 > 0:
	print ("Cant Clientes Abono B: ", cantAbono2)
else:
	print ("No se registraron clientes con abona B")
print("")
if cantAbono1 > 0:
	print ("Cant Clientes Abono C: ", cantAbono3)
else:
	print ("No se registraron clientes con abona C")

porcentajeLlamadas = (llamadasMas5 * 100) / vueltasCiclo
print ("El porcentaje de Llamas de mas de 5 minutos es: ", porcentajeLlamadas, "%") 
