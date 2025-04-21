import random

numeroRandom = random.randint(1,10)
intentos = 3

while True:

	while True:
		try:
			numJugador = int (input("Ingrese el numero adivinador: "))
			break

		except ValueError:
			print ("ERROR, VUELVE A INGRESAR")

	if numJugador < numeroRandom:
		print ("El numero a adivinar es mayor al que enviaste")
		
		intentos = intentos - 1
		print ("intentos: ", intentos)
		if intentos == 0:
			print ("usaste todos los intentos")
			break

		
	elif numJugador > numeroRandom:
		print ("El numero a adivinar es menor al que enviaste")
		
		intentos = intentos - 1
		print ("intentos: ", intentos)
		if intentos == 0:
			print ("usaste todos los intentos")
			break

	else:
		print ("ADIVINASTE EL NUMERO")
		print (f"te quedaste con {intentos} intentos")
		break

print ("el numero alateorio que se genero fue: ", numeroRandom)