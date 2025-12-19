DESTINO_1 = "Cancún"
DESTINO_2 = "Los Cabos"

TARIFA_CANCUN = 3500.0   
TARIFA_CABOS = 4200.0   

print("=== AEROLÍNEA ===")
print("1.", DESTINO_1, "- $", TARIFA_CANCUN)
print("2.", DESTINO_2, "- $", TARIFA_CABOS)

opcion = int(input("Elige el destino (1 o 2): "))
pasajeros = int(input("Ingresa el número de pasajeros: "))

if opcion == 1:
    total = pasajeros * TARIFA_CANCUN
    destino = DESTINO_1
elif opcion == 2:
    total = pasajeros * TARIFA_CABOS
    destino = DESTINO_2
else:
    print("Opción no válida")
    total = None

if total is not None:
    print("\n--- RESUMEN DEL VUELO ---")
    print("Destino:", destino)
    print("Número de pasajeros:", pasajeros)
    print("Total a pagar: $", total)
