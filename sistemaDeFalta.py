ausentesTot= 0
mayorAusentes = 0
cursoConMayorAusentes = 0


for curso in range (1, 6):
			
	cantidadTotal= int (input(f"Ingresa la cantidad de alumnos Totales del curso {curso}: "))
	cantidadAusentes = int (input("Ingresa la cantidad de alumnos ausentes del curso: "))

	print (f"ausentes vuelta {curso}: {cantidadAusentes}")
	print ("")

	cantidadPresentes = cantidadTotal - cantidadAusentes
	print (f"asistieron {cantidadPresentes} alumnos el dia de hoy")

	porcentajePresentismo = (cantidadPresentes*100) / cantidadTotal
	print (f"El porcentaje de alumnos presentes en el curso {curso} es de : {porcentajePresentismo}%")
	print("")


	if cantidadAusentes > mayorAusentes:
		mayorAusentes = cantidadAusentes
		cursoConMayorAusentes = curso
	
	print ("el curso con mas ausentes fue el curso: ", cursoConMayorAusentes)
	print ("")

	ausentesTot = ausentesTot + cantidadAusentes
	print ("**ausentes totales** entre todos los cursos son: ", ausentesTot)  
	print ("")

