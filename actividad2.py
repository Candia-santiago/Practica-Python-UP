num = int (input("Ingresa un numero: "))
contador = 0
numPar = 0
numImparPositivoCont= 0
numImparPositivoAcu= 0
promedioImparPositivo = 0
numParNegativo = 0
sumaTotal = 0

while contador < 100 and num != 0:
	contador += 1
	print (f"esta es la vuelta {contador} del ciclo")
	
	if num % 2 == 0 and num > 0:
		print ("El numero que enviaste es un numero par")
		numPar += 1
		porcentajeNumPares = (numPar*100) /contador

	if num > 0 and num % 2 != 0:
		print ("Enviaste un numero impar POSITIVO")
		numImparPositivoCont +=1
		numImparPositivoAcu += num
		promedioImparPositivo = numImparPositivoAcu / numImparPositivoCont


	if num < 0 and num % 2 == 0:
		print ("Enviaste un numero PAR NEGATIVO")
		numParNegativo =+ 1

	sumaTotal = sumaTotal + num

	num = int (input("Ingresa un numero: "))

print (f"Porcentaje numero pares: {porcentajeNumPares}%")
print (f"numero pares enviados: {numPar}")
print (f"numero enviado en total: {contador}")
print ("")

print (f"promedio de numeros Impares positivos {promedioImparPositivo}")
print ("")
print ("suma total de todos los numeros es: ", sumaTotal)