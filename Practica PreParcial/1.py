numImpar = 0

numParMultiplo4 = 0
contNumPar = 0
promNumeroPar = 0

num = int (input("Ingrese un numero: "))

while num != 0 or num > 0:
	if num % 2 != 0:
		numImpar += 1

	if num % 2 == 0 and num % 4 == 0:
		numParMultiplo4 += num
		contNumPar += 1

	num = int (input("Ingrese un numero: "))

print ("-----Resultados------")
if numImpar > 0:
	print ("La cantidad de numeos impares es: ", numImpar)
else:
	print ("No se enviaron Numeros impares")

if contNumPar > 0:
	promNumeroPar = numParMultiplo4 / contNumPar
	print ("El promedio de numeros pares multiplos de 4 es: ", promNumeroPar)

else:
	print ("No se enviaron num pares multiplos de 4")
