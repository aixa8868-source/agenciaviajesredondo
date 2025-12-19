destino1 = "Centro"
tarifa_destino1 = 50

destino2 = "Aeropuerto"
tarifa_destino2 = 80

costo_por_pasajero = 20

print("=== DESTINOS DISPONIBLES ===")
print("1.", destino1)
print("2.", destino2)

opcion = int(input("Elige el destino (1 o 2): "))
pasajeros = int(input("Ingresa el número de pasajeros: "))

if opcion == 1:
    destino = destino1
    tarifa_base = tarifa_destino1
elif opcion == 2:
    destino = destino2
    tarifa_base = tarifa_destino2
else:
    print("Opción no válida")
    exit()

total_pagar = tarifa_base + (pasajeros * costo_por_pasajero)

print("\n--- RESUMEN DEL VIAJE ---")
print("Destino:", destino)
print("Pasajeros:", pasajeros)
print("Tarifa base: $", tarifa_base)
print("Costo por pasajero: $", costo_por_pasajero)
print("Total a pagar: $", total_pagar)