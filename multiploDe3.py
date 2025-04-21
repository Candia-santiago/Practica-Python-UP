num = int (input("Ingresa un numero: "))


while num % 3 != 0:

	print ("Enviaste un numero que NO es multiplo de 3")
	print ("num: ", num)

	num = int (input("Ingresa un numero: "))

print ("Enviaste un numero que es multiplo de 3")
print("ultimo numero enviado: ", num)