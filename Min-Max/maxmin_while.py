nro = int(input("Ingrese un numero: "))
max = 0

while nro != 0:
    if max ==  0 or nro > max:
        max = nro

    nro = int(input("Ingrese otro numero"))

if max == 0:
    print("No se puede determinar el maximo, sin datos")
else:
    print(max)

    