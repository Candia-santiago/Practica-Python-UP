precioBiciPaseo = 100
precioBiciTerreno = 200

cantVentas = 0
cantTotBiciVendidas = 0

biciT = 0

biciP = 0
promBiciP = 0

recaudadoBiciP = 0
totRecaudadoBiciP= 0
totRecaudadoBiciT = 0
recaudadoBiciT = 0
racaudadoTotal = 0

porcentajeBiciP = 0
porcentajeBiciT = 0

mayorComprador = 0
nomMayorComprador = ""
tipoBiciMayorComprador = ""

print ("Precio Bici paseo : ", precioBiciPaseo, "Precio bici todo terreno: ", precioBiciTerreno)
nroFactura = int (input("Ingrese el numero de la factura: "))
while nroFactura < -1:
	nroFactura = int (input("ERROR, Ingrese el numero de la factura: "))

while nroFactura != -1 and cantVentas < 5:
	cantVentas +=1

	tipoBici = input ("Tipo de bicicleta que lleva: (1-Paseo (p)/ 2-Todo Terreno (t))")
	while tipoBici != "p" and tipoBici != "t":
		tipoBici = input ("ERROR, Tipo de bicicleta que lleva: (1-Paseo (p)/ 2-Todo Terreno (t))")

	nom = input ("Ingrese su nombre: ")
	while nom == "":
		nom = input ("ERROR, Ingrese su nombre: ")

	cantBici = int (input("Cuantas bicicletas lleva?: "))
	while cantBici <= 0:
		cantBici = int (input("ERROR, Cuantas bicicletas lleva?: "))


	cantTotBiciVendidas += cantBici 

	if tipoBici == "p":
		biciP += 1
		recaudadoBiciP = cantBici * precioBiciPaseo
		totRecaudadoBiciP += recaudadoBiciP


	elif tipoBici == "t":
		biciT += 1
		recaudadoBiciT = cantBici * precioBiciTerreno
		totRecaudadoBiciT += recaudadoBiciT

	if mayorComprador == 0 or cantBici > mayorComprador:
		mayorComprador = cantBici
		nomMayorComprador = nom
		tipoBiciMayorComprador = tipoBici

	if cantVentas <= 5:
		nroFactura = int (input("Ingrese el numero de la factura: "))
		while nroFactura < -2:
				nroFactura = int (input("ERROR, Ingrese el numero de la factura: "))

print ("------Resultados-------")
if cantTotBiciVendidas > 0:
		print ("El total de bicletas vendidas es: ", cantTotBiciVendidas)
else:
	print ("No se vendieron bicicletas")

if biciP > 0:
	promBiciP = biciP / cantVentas
	print ("El promedio de ventas de bicicletas de paseo es: ", promBiciP)
else:
	print ("No se vendiron bicis de paseo")

racaudadoTotal = totRecaudadoBiciP + totRecaudadoBiciT
print ("El total recaudado en monto es: ", racaudadoTotal)

if racaudadoTotal > 0:
	porcentajeBiciP = (totRecaudadoBiciP *100) / racaudadoTotal
	print ("El porcentaje en pesos de las bicis de paseo es: ", porcentajeBiciP)

	porcentajeBiciT = (totRecaudadoBiciT *100) / racaudadoTotal
	print ("El porcentaje en pesos de las bicis de paseo es: ", porcentajeBiciT)
else: 
	print ("No se vendieron biciletas")

if biciP > biciT:
	print ("Se vendieron mas unidades de las bicis de paseo")
elif biciP < biciT:
	print ("Se vendieron mas unidades de las biciletas todo terreno")
else:
	print ("Se venideron en cantidades iguales")

print ("El nombre de la persona que mas bicicletas compro es: ", nomMayorComprador, "y se llevo bicletas de tipo: ", tipoBiciMayorComprador)

