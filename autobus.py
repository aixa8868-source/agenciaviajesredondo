tarifa_por_pasajero = 25.0

destino = input("Ingrese el destino del autobús: ")
pasajeros = int(input("Ingrese el número de pasajeros: "))

total_pagar = pasajeros * tarifa_por_pasajero

print("\n--- BOLETO DE AUTOBÚS ---")
print("Destino:", destino)
print("Pasajeros:", pasajeros)
print("Tarifa por pasajero: $", tarifa_por_pasajero)
print("Total a pagar: $", total_pagar)
# autobus dany 