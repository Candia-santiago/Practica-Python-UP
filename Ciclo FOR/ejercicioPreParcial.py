vueltasDelCiclo = 10

numImpar = 0

numMultiploDe5 = 0
acumuladorMultiploDe5 = 0
promMultiplosDe5 = 0

num3o7 = 0

numNegativo = 0
porcentajeNumNega = 0

for i in range (1, vueltasDelCiclo):
	print ("vuelta: ", i)
	num = int (input("Ingrese un num: "))

	if num % 2 != 0 and num > 20:
		numImpar += 1
		if num > numImpar:
			numImpar = num
			print (numImpar)

	if num < 0 and num % 5 == 0:
		numNegativo += 1
		numMultiploDe5 += 1
		acumuladorMultiploDe5 += num
	
	elif num < 0:
		numNegativo += 1

	if num % 3 == 0 or num % 7 == 0:
		num3o7 +=1 



print ("--------Resultados---------")

if numImpar > 0:
	print ("El numero maximo impar mayor a 20 es: ", numImpar)
else:
	print ("No se enviaron numeros impares mayor a 20")

if numMultiploDe5 >0:
	promMultiplosDe5 = acumuladorMultiploDe5 / numMultiploDe5
	print ("Promedio de multiplos de 5 negativos: ", promMultiplosDe5)
else:
	print ("No se enviaron numeros negativos multiplos de 5")

if num3o7 > 0:
	print ("multiplos de 3 o de 7 enviados: ", num3o7)
else:
	print ("No se enviarion multiplos de 3 o de 7")

if numNegativo > 0:
	porcentajeNumNega = (numNegativo * 100) / vueltasDelCiclo
	print ("El porcentaje de numeros negativos es: ", porcentajeNumNega, "%")
else: 
	print ("No se enviaron numeros negativos")