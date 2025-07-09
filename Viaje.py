distancias = {
    ("Santiago", "Buenos Aires"): 1400,
    ("Santiago", "Mendoza"): 365,
    ("Valparaíso", "Córdoba"): 960,
    ("Puerto Montt", "Bariloche"): 300,
    ("Antofagasta", "Salta"): 1050,
    ("Concepción", "Neuquén"): 800
}

velocidades = {
    "auto": 80,
    "bus": 60,
    "bicicleta": 20,
    "caminando": 5
}

def mostrar_ciudades_disponibles():
    print("\nCiudades disponibles:")
    for origen, destino in distancias.keys():
        print(f" - {origen} <--> {destino}")

def calcular_viaje(origen, destino, medio):
    clave = (origen, destino)
    clave_inversa = (destino, origen)

    if clave in distancias:
        distancia = distancias[clave]
    elif clave_inversa in distancias:
        distancia = distancias[clave_inversa]
    else:
        print("No se encuentra una ruta registrada entre esas ciudades.")
        return

    velocidad = velocidades.get(medio.lower())
    if velocidad is None:
        print("Medio de transporte no válido.")
        return

    tiempo_horas = distancia / velocidad
    distancia_millas = distancia * 0.621371

    print(f"\n== Resultado del viaje {origen} -> {destino} ==")
    print(f"Distancia: {distancia} km ({distancia_millas:.2f} millas)")
    print(f"Duración estimada en {medio.lower()}: {tiempo_horas:.2f} horas")
    print(f"Narrativa: Desde {origen} hasta {destino}, viajando en {medio.lower()} por una distancia de {distancia} km.\n")

def main():
    print("=== Calculadora de viaje Chile - Argentina ===")
    mostrar_ciudades_disponibles()

    while True:
        origen = input("\nIngrese ciudad de origen (o 's' para salir): ").title()
        if origen.lower() == 's':
            print("Saliendo del programa.")
            break
        destino = input("Ingrese ciudad de destino: ").title()
        medio = input("Ingrese medio de transporte (auto, bus, bicicleta, caminando): ").lower()

        calcular_viaje(origen, destino, medio)

if __name__ == "__main__":
    main()
