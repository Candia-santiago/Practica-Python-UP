diaMaxPorKilo = 0
dia = 0

facChoco1 = 0
facChoco2 = 0
facChoco3 = 0

cantChoco1 = 0
cantChoco2 = 0
cantChoco3 = 0

ventas = 0

vendedor = ""
acumuladorPedro = 0
acumuladorPablo = 0

contadorVentasPedro = 0
vendedorMaxFacturacion = ""

facturacionVentaActual = 0
diaMaxPorPlata = 0
diaPlata = 0 

print ("Amargo-$100, Dulce-$200, Con Almendras-$500")
for i in range (1, 6):
	
	print ("dia del mes: ", i)

	vendedor = input ("Ingrese el nombre del vendedor: (Pedro/Pablo): ").lower()
	while vendedor != "pedro" and vendedor != "pablo":
		vendedor = input ("ERROR,Ingrese el nombre del vendedor: (Pedro/Pablo): ").lower()

	cantChoco = int (input("Ingrese la cantidad de choco: (kg): "))
	while cantChoco < 0:
		cantChoco = int (input("ERROR, Ingrese la cantidad de choco: (kg): "))

	tipoChoco = int (input("tipo de choco: (1-Amargo, 2-Dulce, 3-Con Almendras): "))
	while tipoChoco < 1 or tipoChoco > 3:
		tipoChoco = int (input("ERROR, tipo de choco: (1-Amargo, 2-Dulce, 3-Con Almendras): "))

	ventas += 1

	if i == 0 or cantChoco > diaMaxPorKilo:
		diaMaxPorKilo = cantChoco
		dia = i 

	if tipoChoco == 1:
		precio = 100
		facChoco1 = cantChoco* precio
		cantChoco1 += cantChoco 	
	elif tipoChoco== 2:
		precio = 200
		facChoco2 = cantChoco *precio
		cantChoco2 += cantChoco
	else:
		precio = 500
		facChoco3 = cantChoco*precio
		cantChoco3 += cantChoco 

	facturacionVentaActual = cantChoco * precio
	print (f"el dia actual ({i}) se facturo: {facturacionVentaActual}")


	if i == 0 or facturacionVentaActual > diaMaxPorPlata:
		diaMaxPorPlata = facturacionVentaActual
		vendedorMaxFacturacion = vendedor
		diaPlata = i


	if vendedor == "pedro":
		acumuladorPedro += facturacionVentaActual
		contadorVentasPedro +=1 
	else:
		acumuladorPablo += facturacionVentaActual


print ("-------resultados------------")
print (f"El dia del mes que mas se vendio fue el dia **{dia}** y se vendio {diaMaxPorKilo} kilos")
print ("")
print (f"el dia {diaPlata} del mes se registro el maximo de facturacion ({diaMaxPorPlata}) a nombre del vendedor: {vendedorMaxFacturacion}")
print ("")

if acumuladorPablo > acumuladorPedro:
	print ("Pablo facturo mas que pedro")
else:
	print ("Pedro facturo mas que pablo")
print ("")

print ("Kilos vendidos de chocolate Amargo: ", cantChoco1,"kg")
print ("Kilos vendidos de chocolate Dulce: ", cantChoco2,"kg")
print ("Kilos vendidos de chocolate Con Almendras: ", cantChoco3,"kg")
print ("")

if contadorVentasPedro > 0:
	porcentajeVentasPedro = (contadorVentasPedro * 100) / ventas
	print ("El porcentaje de ventas de pedro es : ", porcentajeVentasPedro, "%")
else:
	print ("Pedro no tuvo ventas a su cargo")
print ("----------------------------")