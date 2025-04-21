while True:

	while True:
		try:
			num1 = int(input("ingrese un numero: "))
			break

		except ValueError:
			print("Ingresaste mal el numero, Ingreselo nuevamente")

	while True:
		try:
			num2 = int(input("ingrese otro numero: "))
			break

		except ValueError:
			print ("error al ingresar el numero, Ingreselo nuevamente")

	opcOperadores = str(input("Ingresa la operacion que queres realizar: "))

	if opcOperadores == "-":
		resultadoResta = num1 - num2
		print (resultadoResta)

	elif opcOperadores == "+":
		resultadoSuma = num1+num2
		print (resultadoSuma)

	elif opcOperadores == "*":
		resultadoMulti = num1 * num2
		print (resultadoMulti)

	elif opcOperadores.lower() == "potencia":
		resultadoPot = num1 ** num2
		print(resultadoPot)

	elif opcOperadores == "/":
		if num2 == 0:
			print ("NO se puede dividir por 0, OPERACION INVALIDA")
		else:
			resultadoDivision = num1 / num2
			print (resultadoDivision)
	else:
		print ("**Operador invalido**")

	opcContinuar = str(input("quiere continuar? si/no: " )).lower()

	if opcContinuar == "no":
		print ("Se cierra la calculadora")
		break