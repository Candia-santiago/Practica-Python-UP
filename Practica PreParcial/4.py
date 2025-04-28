precioMemoria = 100
precioCpu = 200
precioDisco = 300

prod1 = 0
prod2 = 0
prod3 = 0

facturacionDeCompraP1 = 0
facTotProd1 = 0
facturacionDeCompraP2 = 0
facTotProd2 = 0
facturacionDeCompraP3 = 0
facTotProd3 = 0
totFacturado = 0

mayorImporte = 0

menorCantidad =0
nroFacturaMenorCantidad = 0

ventasTot = 0
promVentasP1 = 0
promVentasP2 = 0
promVentasP3 = 0


nroFactura = int (input("Ingrese su numero de factura: "))
while nroFactura < 0:
	nroFactura = int (input("ERROR, Ingrese su numero de factura: "))

while nroFactura != 0:
	ventasTot += 1

	nom = input ("Ingrese su nombre: ")
	while nom == "":
		nom = input ("ERROR, Ingrese su nombre: ")

	prod = int (input("Seleccione un producto: 1-Memoria/2-CPU/Disco (1/2/3): "))
	while prod < 1 or prod > 3:
		prod = int (input("ERROR, Seleccione un producto: 1-Memoria/2-CPU/Disco (1/2/3): "))

	cant = int (input("Cuantos productos se lleva: "))
	while cant < 0:
		cant = int (input("ERROR, Cuantos productos se lleva: "))

	if prod == 1:
		prod1 += 1
		facturacionDeCompraP1 = cant * precioMemoria
		facTotProd1 += facturacionDeCompraP1
		if mayorImporte == 0 or facturacionDeCompraP1 > mayorImporte:
			mayorImporte = facturacionDeCompraP1

	elif prod == 2:
		prod2 += 1
		facturacionDeCompraP2 = cant * precioCpu
		facTotProd2 += facturacionDeCompraP2
		if mayorImporte == 0 or facturacionDeCompraP2 > mayorImporte:
			mayorImporte = facturacionDeCompraP2

	else:
		prod3 += 1
		facturacionDeCompraP3 = cant * precioDisco
		facTotProd3 += facturacionDeCompraP3
		if mayorImporte == 0 or facturacionDeCompraP3 > mayorImporte:
			mayorImporte = facturacionDeCompraP3

	if menorCantidad == 0 or cant < menorCantidad:
		menorCantidad = cant
		nroFacturaMenorCantidad = nroFactura

	nroFactura = int (input("Ingrese su numero de factura: "))
	while nroFactura < 0:
		nroFactura = int (input("ERROR, Ingrese su numero de factura: "))


print ("------RESULTADOS-------")
totFacturado = facTotProd1 + facTotProd2 + facTotProd3
print ("El total facturado es: ", totFacturado)

print ("La factura con mayor importe es: ", mayorImporte)
print ("La factura con menor cantidad de art es la factura nro: ", nroFacturaMenorCantidad, "con: ", menorCantidad, "de articulos")

if prod1 > prod2 and prod1 > prod3:
	print ("el producto 1 es el mas vendido")
elif  prod2 > prod1 and prod2 > prod3:
	print ("El producto 2 es el mas vendido")
elif prod1 == prod2 and prod2 == prod3:
	print ("Se vendieron la misma cantidad de los 3 productos")
else:
	print ("El producto 3 es el mas vendido")

if prod1 > 0:
	promVentasP1 = prod1 / ventasTot
	print ("El promedio de ventas del p1 sobre el total de ventas es: ", promVentasP1)
else:
	print ("No se vendieron art N1")

if prod2 > 0:
	promVentasP2 = prod2 / ventasTot
	print ("El promedio de ventas del p2 sobre el total de ventas es: ", promVentasP2)
else:
	print ("No se vendieron art N2")

if prod3 > 0:
	promVentasP3 = prod3 / ventasTot
	print("El promedio de ventas del p3 sobre el total de ventas es: ", promVentasP3)
else:
	print ("No se venieron productos N3")