# viaje.py
import requests

API_KEY = "cbb30c75-a919-45fd-ad9f-5bcc8269fd75"  # Reemplaza con tu key de GraphHopper

def obtener_datos_viaje(origen, destino, transporte):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen, destino],
        "vehicle": transporte,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos:", response.status_code)
        return None

def main():
    print("== Medidor de distancia entre ciudades (Chile - Argentina) ==")
    while True:
        origen = input("Ingrese ciudad de origen (o 's' para salir): ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese ciudad de destino: ")
        print("Tipos de transporte: car, bike, foot")
        transporte = input("Ingrese medio de transporte: ")

        ruta = obtener_datos_viaje(origen, destino, transporte)
        if ruta:
            distancia_km = ruta["paths"][0]["distance"] / 1000
            distancia_mi = distancia_km * 0.621371
            duracion = ruta["paths"][0]["time"] / (1000 * 60)
            narrativa = ruta["paths"][0]["instructions"]

            print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
            print(f"Duración estimada: {duracion:.1f} minutos")
            print("Narrativa del viaje:")
            for paso in narrativa:
                print(f" - {paso['text']}")

if __name__ == "__main__":
    main()
