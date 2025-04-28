turnoMatutino = 0
porcentajeMatutino = 0

totPases = 0

menores18 = 0
acuEdadMenos18 = 0

mayorEdad = 0
turnoMayorEdad = ""

sexoM= 0
sexoF = 0

turno = input ("Ingrese su turno: (1-matutino/2-vespertino): ")
while turno != "FIN":
	while turno != "matutino" and turno != "vespertino":
		turno = input ("ERROR, Ingrese su turno: (1-matutino/2-vespertino): ")
	totPases += 1

	edad = int (input("Ingrese su edad: "))
	while edad < 0:
		edad = int (input("ERROR, Ingrese su edad: "))

	sexo = int (input("Ingrese su sexo (1-Masculino/2-femenino)"))
	while sexo < 0 and sexo > 2:
		sexo = int (input("ERROR, Ingrese su sexo (1-Masculino/2-femenino)"))

	if turno == "matutino":
		turnoMatutino += 1

	if edad < 18:
		menores18 += 1
		acuEdadMenos18 += edad 

	if mayorEdad == 0 or edad > mayorEdad:
		mayorEdad = edad
		turnoMayorEdad = turno

	if sexo == 1:
		sexoM += 1
	else:
		sexoF += 1

	turno = input ("Ingrese su turno: (1-matutino/2-vespertino): ")


print ("----Resultados----")
if turnoMatutino > 0:
	porcentajeMatutino = (turnoMatutino * 100) / totPases
	print ("El porcentaje de pases matutinos es: ", porcentajeMatutino, "%")
else: 
	print ("No se registraron pases matutinos")

if menores18 > 0:
	promMenor18 = acuEdadMenos18 / menores18
	print ("El promedio de edad de los menores a 18 es: ", promMenor18)
else:
	print ("No se registraron pases para menores a 18")

print ("La mayor edad reistrada es: ", mayorEdad, "en el turno: ", turnoMayorEdad)

if sexoM > 0:
	print ("Hombres ristrados: ", sexoM)
else:
	print("No se registraron Hombres")

if sexoF> 0:
	print ("Mujeres ristrados: ", sexoF)
else:
	print("No se registraron Mujeres")