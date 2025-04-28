vueltasDelCiclo = 6

acumuMultiplosDe7 = 0
contMultiplosDe7 = 0

multiplosExclusivo5 = 0
multiplo3y5= 0
porcentaje = 0

numMenor = 0

for i in range(1, vueltasDelCiclo + 1 ):
	num = int (input("Ingrese un num: "))

	if num < 0 and num % 7 == 0:
		acumuMultiplosDe7 += num
		print ("acumulador num negativos multiplos de 7: ", acumuMultiplosDe7)
		contMultiplosDe7 += 1
		print ("contador num negativos multiplos de 7: ",contMultiplosDe7 )

	if num % 5 == 0:
		print ("El numero es multiplo de 5")
		if num % 3 == 0:
			multiplo3y5 += 1
			print ("El numero es multiplo de 5 y tambien de 3")
		else:
			print ("El numero es unicamente multiplo de 5 y no de 3")
			multiplosExclusivo5 += 1

	if i == 0 or num < numMenor: 
		numMenor = num

print ("-----Resultados-----")
if contMultiplosDe7 > 0:
	promMultiplos7 = acumuMultiplosDe7 / contMultiplosDe7
	print ("El promedio de num Negativos multiplos de 7 es: ", promMultiplos7)
else:
	print ("No enviaron numeros negativos multiplos de 7")

porcentaje = (multiplosExclusivo5 * 100) / vueltasDelCiclo  
print ("El porcentaje de numeros multiplos de 5 pero NO de 3 es: ", porcentaje, "%")

print ("El menor numero enviado es: ", numMenor)