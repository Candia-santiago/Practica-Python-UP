categoria1 = 0
categoria2 = 0
categoria3 = 0
categoria4 = 0
sueldoTot = 0
print ("CATEGORIA 1: $150, CATEGORIA 2: $200, CATEGORIA 3: $250, CATEGORIA 4: $280")

categoria = int (input("Ingrese la categoria del empleado: (1-cat1, 2-cat2, 3-cat3, 4-cat4)"))
horasTrabajadas = int (input("Ingresa la cantidad de hs trabajadas: "))

while categoria > 0 and categoria <4 :
	if categoria == 1:
		categoria1 +=1

		sueldoBruto = horasTrabajadas*150
		print ("El sueldo bruto es: ", sueldoBruto) 

		descuentoSueldo = sueldoBruto - (sueldoBruto*0.83)
		sueldoNeto = sueldoBruto - descuentoSueldo
		print ("El sueldo neto es:", sueldoNeto)

		print ("la cantidad de empleados en esta categoria es: ", categoria1)

	elif categoria == 2:
		categoria2 +=1

		sueldoBruto = horasTrabajadas*200
		print ("El sueldo bruto es: ", sueldoBruto) 

		descuentoSueldo = sueldoBruto - (sueldoBruto*0.83)
		sueldoNeto = sueldoBruto - descuentoSueldo
		print ("El sueldo neto es:", sueldoNeto)

		print ("la cantidad de empleados en esta categoria es: ", categoria2)

	elif categoria ==3:
		categoria3 +=1

		descuentoSueldo = sueldoBruto - (sueldoBruto*0.83)
		sueldoNeto = sueldoBruto - descuentoSueldo
		print ("El sueldo bruto es:", sueldoNeto)

		sueldoNeto = sueldoBruto - (sueldoBruto*0.83)
		print ("El sueldo neto es:", sueldoNeto)

		print ("la cantidad de empleados en esta categoria es: ", categoria3)

	elif categoria == 4:
		categoria4 +=1

		sueldoBruto = horasTrabajadas*280
		print ("El sueldo bruto es: ", sueldoBruto) 

		descuentoSueldo = sueldoBruto - (sueldoBruto*0.83)
		sueldoNeto = sueldoBruto - descuentoSueldo
		print ("El sueldo neto es:", sueldoNeto)

		print ("la cantidad de empleados en esta categoria es: ", categoria4)

	sueldoTot = sueldoTot+sueldoBruto


	categoria = int (input("Ingrese la categoria del empleado: (1-cat1, 2-cat2, 3-cat3, 4-cat4)"))
	horasTrabajadas = int (input("Ingresa la cantidad de hs trabajadas: "))

print ("El total de sueldos que paga la empresa es: ",sueldoTot)
