hombreMas45 = 0
mujeres= 0

contadorPrimario = 0
acumuladorPrimariaEdad = 0
promPrimaria = 0

promSecundaria = 0
contadorSecundario = 0
acumuladorSecundariaEdad = 0

contadorTerciario= 0
acumuladorTerciarioEdad = 0
promTerciario = 0

mujerEstudioTerciario = 0
porcentajeMujeresTerciario = 0

hMas30 = 0
porcentaeHombre = 0
hombres = 0

mujeresMas40 = 0
acumuladorMujeresMas40 = 0
promMujeresMas40 = 0

for i in range (1, 6):
	
	edad = int (input("Ingrese su edad: "))
	while edad < 0:
		edad = int (input("ERROR, vuelva a ingresar la edad: "))

	sexo = int (input("Seleccione su sexo 1-Masculino/ 2-Femenino: "))
	while sexo < 0 or sexo > 2:
		sexo = int (input("ERROR, seleccione una opcion valida: "))

	estudiosCursados = int(input("Estudios obtenidos: 1-primario/ 2-secundario/ 3-terciario: "))
	while estudiosCursados < 0 or estudiosCursados > 3:
		estudiosCursados = int (input("ERROR, Ingrese una opcion valida: "))

	if sexo == 1:
		hombres += 1
		if edad > 45:
			hombreMas45 += 1

	else:
		mujeres += 1


	if estudiosCursados == 1:
		contadorPrimario += 1
		acumuladorPrimariaEdad += edad

	elif estudiosCursados == 2:
		contadorSecundario += 1
		acumuladorSecundariaEdad += edad 
		if sexo == 2 and edad > 40:
			mujeresMas40 += 1
			acumuladorMujeresMas40 += edad

	
	elif estudiosCursados == 3:
		contadorTerciario += 1
		acumuladorTerciarioEdad += edad
		if sexo == 2:
			mujerEstudioTerciario += 1
		else:
			if edad >30:
				hMas30 += 1

print ("-------Resultados---------")

print ("Hombres encuestados: ", hombres)
print ("Mujeres encuestadas: ", mujeres)
print ("")
if contadorPrimario >= 1:
	promPrimaria = acumuladorPrimariaEdad/contadorPrimario
	print ("Promedio de edad de personas que terminaron la primaria: ", promPrimaria)
else :
	print ("NO se registaron personas con el primario")

print ("")
if contadorSecundario >= 1:
	promSecundaria = acumuladorSecundariaEdad/ contadorSecundario
	print ("Promedio edad Secundario: ", promSecundaria)
else: 
	print ("No se registraron personas con el secundario")

print ("")
if contadorTerciario >= 1:
	promTerciario = acumuladorTerciarioEdad / contadorTerciario
	print ("Promedio edad Terciario: ", promTerciario)
else:
	print ("NO se registarin personas con un terciario")

print ("")
if mujerEstudioTerciario >= 1:
	porcentajeMujeresTerciario = (mujerEstudioTerciario *100) / mujeres
	print ("El porcentaje de mujeres con terciario es: ", porcentajeMujeresTerciario,"%")
else :
	Print ("NO SE PUEDO HACER EL PORCENTAJE DE MUJERES")

print ("")
if hMas30 >= 1:
	porcentaeHombre = (hMas30 *100) / hombres
	print ("Porcentaje de hombres +30 con terciario: ", porcentaeHombre,"%")
else :
	print ("NO SE PUDO HACER EL PORCENTAJE DE LOS HOMBRES")

print ("")
if mujeresMas40 >= 1:
	promMujeresMas40 = acumuladorMujeresMas40 / mujeresMas40
	print ("Promedio de edad mujeres Mas 40 con secundario: ", promMujeresMas40)
else: 
	print ("No hay mujeres +40 con secundario")
print ("----------------------------")