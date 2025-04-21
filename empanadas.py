cantEmpandaFritas = 0
cantEmpandaDulce = 0
cantEmpandaHorno = 0

mayorComprador = 0
direcMayorComprador = 0

direccionesMas15Horno = []

cantEmpanadas = int (input("Ingrese la cantidad de empandas: "))

while cantEmpanadas !=0:

	print ("Tarifa de cada empanda: horno-$100, 2-Frita-$150,, 3-Dulce-$200 ")
	tipoEmpanda = int (input("Elija su empanda: 1-Horno, 2-Frita, 3-Dulce: "))
	direc =  int(input ("Ingrese la direccion del domicilio: "))

	if tipoEmpanda == 1:
		cantEmpandaHorno = cantEmpandaHorno + cantEmpanadas

		if cantEmpanadas > 15:
			print ("la direccion es; ", direc)
			direccionesMas15Horno.append(direc)


	elif tipoEmpanda == 2:
		cantEmpandaFritas = cantEmpandaFritas + cantEmpanadas

	elif tipoEmpanda == 3:
		cantEmpandaDulce = cantEmpandaDulce + cantEmpanadas

	if cantEmpanadas > mayorComprador:
		mayorComprador = cantEmpanadas
		direcMayorComprador = direc


	cantEmpanadas = int (input("Ingrese la cantidad de empandas: "))

print (f"Se vendieron: {cantEmpandaHorno} empandas al horno, {cantEmpandaFritas} empanadas Fritas, {cantEmpandaDulce} empanadas dulces") 

totalRecaudado = (cantEmpandaHorno*100) + (cantEmpandaFritas *150) + (cantEmpandaDulce*200)
print ("El total recaudado es : ", totalRecaudado)

print ("La direccion del mayor comprador es: ", direcMayorComprador)

if len(direccionesMas15Horno) > 0:
    print("Direcciones que compraron más de 15 empanadas al horno:")
    for d in direccionesMas15Horno:
        print("-", d)
else:
    print("Ninguna dirección compró más de 15 empanadas al horno.")