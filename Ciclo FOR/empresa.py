sueldoMas20k = 0
totSueldos = 0

empleadosCat1= 0

sueldoMayor= 0
nomMayorSueldo = ""

sueldoCat1 = 0
sueldoCat2= 0
sueldoCat3= 0

for i in range (1, 11):
	nom = input ("Ingrese su nombre: ")

	sueldo = int (input("Ingrese su sueldo: "))
	while sueldo < 0:
		sueldo = int (input("ERROR, vuelva a ingresar su sueldo"))

	cat = int (input("Ingrese su categoria: (1/ 2/ 3); "))
	while cat < 1 or cat > 3:
		cat = int (input("ERROR, Ingrese su categoria: (1/ 2/ 3); "))

	totSueldos += sueldo
	if sueldo > 20000:
		sueldoMas20k += 1 
		print ("Sueldo mayor a $20.000")

	if sueldo < 5000 and cat == 1:
		empleadosCat1 += 1

	if sueldo > sueldoMayor:
		sueldoMayor = sueldo
		nomMayorSueldo = nom

	if cat == 1:
		sueldoCat1 += sueldo
	elif cat == 2:
		sueldoCat2 += sueldo
	else:
		sueldoCat3 += sueldo 

print ("-------Resultados-------") 
print ("El total que tiene que pagar la empresa de sueldos es: ", totSueldos)
print ("")

if sueldoMas20k > 0:
	print ("La cantidad de empleados que cobran mas de 20k es: ", sueldoMas20k)
else: 
	print ("No se registro ningun sueldo mayor a $20.000")
print("")

if empleadosCat1 > 0:
	print("Empleados menos de 5k y cat 1: ", empleadosCat1)
else:
	print ("NO se registro ningun empleado que cumpla con los requisitos")
print ("")

print ("Nombre de empleado con mayor sueldo: ", nomMayorSueldo, "cobra: ", sueldoMayor)
print ("")

print ("Sueldos de la cat 1: ", sueldoCat1)
print ("Sueldos de la cat 2: ", sueldoCat2)
print ("Sueldos de la cat 3: ", sueldoCat3)
print ("-----------------------------------")