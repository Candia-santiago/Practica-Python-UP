potencia = 0
for num in range (1, 11):
	
	numero = int (input("ingresa el primer numero de la operacion: "))
	opc = int (input("seleccione la operacion: 1-factorizacion, 2-potenciacion, 3-x operacion: "))

	if opc == 1:
		factorial = 1
		for i in range (1, numero + 1):
			factorial *= i
		
		print (f"Resultado del factorial del numero {numero} es:  {factorial}")

	elif opc == 2:
		exponente = int (input("Ingresa el exponente de la potencia (x a la n): "))
		potencia = numero ** exponente
		print (f"El resultado de la potencia de {numero} elevado a {exponente} es : {potencia}")

	elif opc == 3:
		
		if numero == 0:
			print ("el numero es nulo")

		elif numero % 2 == 0:
			print ("el numero es par")

		elif numero % 2 != 0:
			print ("el numero es impar")
