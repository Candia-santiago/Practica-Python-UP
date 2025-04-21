total_butacas_vendidas = 0
salas_con_todo_vendido = 0

max_butacas_vendidas = 0
min_butacas_vendidas = 0
sala_max = 0
sala_min = 0

for i in range(15):
    print(f"Sala {i + 1}")

    numero_sala = int(input("Número de sala: "))
    while numero_sala <= 0:
        numero_sala = int(input("Número inválido. Ingrese número de sala (> 0): "))

    total_butacas = int(input("Cantidad total de butacas: "))
    while total_butacas <= 0:
        total_butacas = int(input("Cantidad inválida. Ingrese cantidad total de butacas (> 0): "))

    butacas_vendidas = int(input("Cantidad de butacas vendidas: "))
    while butacas_vendidas < 0 or butacas_vendidas > total_butacas:
        butacas_vendidas = int(input("Cantidad inválida. Ingrese butacas vendidas (0 a total): "))

    total_butacas_vendidas += butacas_vendidas

    if butacas_vendidas == total_butacas:
        salas_con_todo_vendido += 1

    porcentaje = (butacas_vendidas / total_butacas) * 100
    print(f"Porcentaje de butacas vendidas: {porcentaje}%")

    if i == 0:
        max_butacas_vendidas = butacas_vendidas
        min_butacas_vendidas = butacas_vendidas
        sala_max = numero_sala
        sala_min = numero_sala
    else:
        if butacas_vendidas < min_butacas_vendidas:
            min_butacas_vendidas = butacas_vendidas
            sala_min = numero_sala

        if butacas_vendidas > max_butacas_vendidas:
            max_butacas_vendidas = butacas_vendidas
            sala_max = numero_sala

promedio = total_butacas_vendidas / 15

print("\n--- Resultados finales ---")
print(f"a) Sala con menor cantidad de butacas vendidas: {sala_min}")
print(f"b) (Porcentajes ya mostrados durante la carga)")
print(f"c) Salas que vendieron todas las butacas: {salas_con_todo_vendido}")
print(f"d) Promedio de butacas vendidas en todo el cine: {promedio}")
print(f"e) Sala con mayor cantidad de butacas vendidas: {sala_max}")
