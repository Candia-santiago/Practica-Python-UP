print ("Tarifas de camiones: 1-$150, 2-$200, 3-$300")
viajesCamion1= 0
viajesCamion2= 0
viajesCamion3= 0

hsCamion1= 0
hsCamion2= 0
hsCamion3= 0

interior = 0
capital = 1

print ("**CARGAR BOLETA**")
nroDeViaje = int (input("Ingrese el numero de viaje: "))

while nroDeViaje < 0:
	print ("ERROR, vuelve a ingresar el numero de viaje")
	nroDeViaje = int (input("Ingrese el numero de viaje: "))

while nroDeViaje != 0:

	nroCamion = int (input("Seleccione la tarifa del camion (1/2/3): "))
	while nroCamion < 1 or nroCamion > 3:
		print("ERROR, Las tarifas son del 1 al 3, vuelva a ingresar la tarifa")
		nroCamion = int (input("Seleccione la tarifa del camion (1/2/3): "))


	hsTrabajadas = int (input("Ingrese las hs trabajadas: "))
	while hsTrabajadas <= 0:
		print ("ERROR, Ingrese las horas trabajadas")
		hsTrabajadas = int (input("Ingrese las hs trabajadas: "))


	destino = int(input("1-interior, 2-capital: "))
	while destino < 1 or destino > 2:
		print ("ERROR, Elija opcion 1 o opcion 2")
		destino = int(input("1-interior, 2-capital: "))

	if nroCamion == 1:
		viajesCamion1 +=1

		recaudadoCamion1 = hsTrabajadas*150
		hsCamion1 += hsTrabajadas
		
		if destino == 1:
			interior +=1
		else:
			capital+=1

	elif nroCamion == 2:
		viajesCamion2 +=1

		recaudadoCamion2 = hsTrabajadas*200
		hsCamion2 += hsTrabajadas
		
		if destino == 1:
			interior +=1
		else:
			capital+=1

	elif nroCamion == 3:
		viajesCamion3 += 1

		recaudadoCamion3 = hsTrabajadas*300
		hsCamion3 += hsTrabajadas
		
		if destino == 1:
			interior +=1
		else:
			capital+=1

	print("\n--- TICKET DE BOLETA ---")
	print(f"Nro de viaje: {nroDeViaje}")
	print(f"Nro de camión: {nroCamion}")
	print(f"Horas trabajadas: {hsTrabajadas}")
	print(f"Destino: {destino}")
	print("------------------------\n")

	print ("**CARGAR BOLETA**")
	nroDeViaje = int (input("Ingrese el numero de viaje: "))


totalRecaudado = recaudadoCamion1+ recaudadoCamion2+recaudadoCamion3
print ("Lo recaudado en total es: ", totalRecaudado)

viajesTot = viajesCamion2+ viajesCamion1+ viajesCamion3
print ("La cantidad de viajes en total es: ", viajesTot)

print (f"viajes camion 1: {viajesCamion1}, viajes camion 2: {viajesCamion2}, viajes camion 3: {viajesCamion3}")

print (f"horas camion 1: {hsCamion1}, horas camion 2: {hsCamion2}, horas camion 3: {hsCamion3}")

print (f"Al interior hubo un total de {interior} viajes")
