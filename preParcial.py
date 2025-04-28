pedidos = 0

mandarina = 0
mandarinaCaba = 0
mandarinaGBA = 0
porcentajeMandarina = 0

cantNaranjasCaba = 0
pedidoDeNaranjas = 0
cantNaranjas = 0
promNaranjas = 0

cantMax = 0

cant = int (input("Ingrese la cantidad del producto que lleva: "))
while cant < 0:
	cant = int (input("ERROR, Ingrese la cantidad del producto que lleva: "))

while cant != 0:
	pedidos += 1
	numPedido = int (input("Ingrese el numero del pedido: "))
	while numPedido < 0:
		numPedido = int (input("ERROR, Ingrese el numero del pedido: "))

	citrico = int (input("Que citrico lleva: (1-Pomelo/2-Naranja/3-Mandarina): "))
	while citrico < 0 or citrico > 3:
		citrico = int (input("ERROR, Que citrico lleva: (1-Pomelo/2-Naranja/3-Mandarina): "))

	ubiCliente = input ("Destino del pedido: (CABA o GBA): ")
	while ubiCliente != "CABA" and ubiCliente != "GBA":
		ubiCliente = input ("ERROR, Destino del pedido: (CABA o GBA): ")

	if citrico == 3:
		mandarina +=1
		if ubiCliente == "CABA":
			mandarinaCaba += 1
		else:
			mandarinaGBA +=1

	if citrico == 2 and ubiCliente == "CABA":
		cantNaranjasCaba += cant
		cantNaranjas += cant
		pedidoDeNaranjas += 1
		print (cantNaranjas)
	elif citrico == 2:
		pedidoDeNaranjas += 1
		cantNaranjas += cant
		print (cantNaranjas)

	if cantMax == 0 or cant > cantMax:
		cantMax = cant
		nroPedidoMax = numPedido

	cant = int (input("Ingrese la cantidad del producto que lleva: "))
	while cant < 0:
		cant = int (input("ERROR, Ingrese la cantidad del producto que lleva: "))

print ("--------Resultados--------")
if mandarina > 0:
	porcentajeMandarina = (mandarina * 100) / pedidos
	print ("El porcentaje de pedidos de mandarinas es: ", porcentajeMandarina)
	if mandarinaCaba > mandarinaGBA:
		print ("Se vendireron mas mandarinas en caba")
	else:
		print ("Se vendireron mas mandarinas en GBA")
print ("")
if cantNaranjasCaba > 0:
	print ("Tot de naranjas enviados a caba es: ", cantNaranjasCaba)
else:
	print ("No se enviaron Naranjas a caba")
print ("")

if pedidoDeNaranjas > 0:
	promNaranjas = cantNaranjas / pedidoDeNaranjas
	print ("Promedio de naranjas por pedido: ", promNaranjas)

if cantMax > 0:
	print ("la cantidad maxima de unidades vendidas en un pedido es: ", cantMax, "del pedido nro: ", nroPedidoMax)
else:
	print ("NO se registro ninguna venta")