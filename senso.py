hmas45 = 0
mujeres = 0

acumuladorEdadPrimaria = 0
acumuladorCarreraPrimaria = 0
promedioEdadCarreraPrimaria = 0

acumuladorEdadSecundaria = 0
acumuladorCarreraSecundaria = 0
promedioEdadCarreraSecundaria = 0

acumuladorEdadTerciarios = 0
acumuladorCarreraTerciarios = 0
promedioEdadCarreraTerciarios = 0

mujeresTerciario = 0
porcetajeMujeres = 0

hmas30Terciario = 0
porcetajeHombres= 0
hombres = 0

edadProm = 0
contadorEdad = 0
mujerMas40 = 0

edad = int(input("Ingrese su edad: "))
while edad < 0 or edad > 120:
    print("ERROR, ingreso mal la edad")
    edad = int(input("Ingrese su edad: "))


estudiosCursados = int (input("Ingrese sus estudios: 1-Primario Completo, 2-Secuandario Completo, 3-Estudios Terciarios: "))
while estudiosCursados < 1 or estudiosCursados >3:
	print ("ERROR, ingrese del 1 al 3")
	estudiosCursados = int (input("Ingrese sus estudios: 1-Primario Completo, 2-Secuandario Completo, 3-Estudios Terciarios: "))


while edad != 0 and estudiosCursados != 0:
	sexo = int(input("Ingrese su sexo: 1-M, 2-F: ")) 
	while sexo < 1 or sexo >2:
		print ("ERROR, ingreso mal el sexo")
		sexo = int(input("Ingrese su sexo: 1-M, 2-F: ")) 

	if sexo == 1:
		hombres += 1
		if edad > 45: 
			hmas45 += 1
			print ("existem Hombre con mas de 45 años: ", hmas45) 

	elif sexo == 2:
		mujeres +=1
		print ("contador de mujeres encuestadas: ", mujeres) 


	if estudiosCursados == 1:
		acumuladorEdadPrimaria += edad
		acumuladorCarreraPrimaria+= 1
		print (F"acumulador edad: {acumuladorEdadPrimaria}, acumulador acumuladorCarreraPrimaria: {acumuladorCarreraPrimaria}")

		promedioEdadCarreraPrimaria = acumuladorEdadPrimaria /acumuladorCarreraPrimaria

	elif estudiosCursados == 2:
		acumuladorEdadSecundaria += edad
		acumuladorCarreraSecundaria+= 1
		print (F"acumulador edad: {acumuladorEdadSecundaria}, acumulador acumuladorCarreraPrimaria: {acumuladorCarreraSecundaria}")

		promedioEdadCarreraSecundaria = acumuladorEdadSecundaria /acumuladorCarreraSecundaria

	elif estudiosCursados == 3:

		acumuladorEdadTerciarios += edad
		acumuladorCarreraTerciarios+= 1
		print (F"acumulador edad: {acumuladorEdadTerciarios}, acumulador acumuladorCarreraPrimaria: {acumuladorCarreraTerciarios}")

		promedioEdadCarreraTerciarios = acumuladorEdadTerciarios /acumuladorCarreraTerciarios


		if sexo == 2 and estudiosCursados == 3:
			mujeresTerciario += 1
			porcetajeMujeres = (mujeresTerciario*100) / mujeres

		if sexo == 1 and edad == 30 and estudiosCursados == 3:
			hmas30Terciario += 1
			porcetajeHombres = (hmas30Terciario*100) / hombres
		
		if sexo == 2 and edad > 40 and estudiosCursados == 2:
			edadProm += edad
			contadorEdad += 1

			mujerMas40 = edadProm / contadorEdad 

	edad = int (input("Ingrese su edad: "))
	while edad < 0 or edad > 120:
		print ("ERROR, ingreso mal la edad")
		edad = int (input("Ingrese su edad: "))
	
	estudiosCursados = int (input("Ingrese sus estudios: 1-Primario Completo, 2-Secuandario Completo, 3-Estudios Terciarios: "))
	while estudiosCursados == 0 or estudiosCursados >3:
		print ("ERROR, ingrese del 1 al 3")
		estudiosCursados = int (input("Ingrese sus estudios: 1-Primario Completo, 2-Secuandario Completo, 3-Estudios Terciarios: "))


print ("--------RESULTADOS---------")

print ("Hombres censados: ", hombres)
print ("Mujeres censadas: ", mujeres)
print ("------------------------------")
print ("La cantidad de hombres mayores a 45 es: ", hmas45)
print ("La cantidad de mujeres encuestadas es: ", mujeres)
print ("------------------------------")
print ("Cantidad de personas que terminaron la primaria: ", acumuladorCarreraPrimaria)
print ("Cantidad de personas que terminarion el secundario: ", acumuladorCarreraSecundaria)
print ("cantidad de personas que terminarion el teciario: ", acumuladorCarreraTerciarios)
print ("------------------------------")
print ("promedio de edad que terminaron la primaria: ", promedioEdadCarreraPrimaria)
print ("promedio de edad que terminaron la secuandaria: ", promedioEdadCarreraSecundaria)
print ("promedio de edad que terminaron el terciario: ", promedioEdadCarreraTerciarios)
print ("------------------------------")
print ("El porcentaje de mujeres con terciario es: ", porcetajeMujeres)
print ("El porcentaje de hombres +30 con terciario es: ", porcetajeHombres)
print ("-------------------------------------")
print ("Promedio de mujer +40 que tienen secundario es: ", mujerMas40)