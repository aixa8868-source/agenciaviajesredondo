DESTINO_1 = "Mazatlán"
DESTINO_2 = "Puerto Vallarta"

TARIFA_MAZATLAN = 1600.0
TARIFA_VALLARTA = 2000.0

print("=== VIAJES EN BARCO ===")
print("1.", DESTINO_1, "- $", TARIFA_MAZATLAN)
print("2.", DESTINO_2, "- $", TARIFA_VALLARTA)

opcion = int(input("Elige el destino (1 o 2): "))
pasajeros = int(input("Ingresa el número de pasajeros: "))

if opcion == 1:
    total = pasajeros * TARIFA_MAZATLAN
    destino = DESTINO_1
elif opcion == 2:
    total = pasajeros * TARIFA_VALLARTA
    destino = DESTINO_2
else:
    print("Opción no válida")
    total = None

if total is not None:
    print("\n--- RESUMEN DEL VIAJE EN BARCO ---")
    print("Destino:", destino)
    print("Número de pasajeros:", pasajeros)
    print("Total a pagar: $", total)
