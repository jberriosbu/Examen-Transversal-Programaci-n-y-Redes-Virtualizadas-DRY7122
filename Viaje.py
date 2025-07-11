import requests

API_KEY = "3596a944-50c3-4c9d-af7c-98ad80d176ac" 

def obtener_coordenadas(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        if data['hits']:
            lat = data['hits'][0]['point']['lat']
            lng = data['hits'][0]['point']['lng']
            return f"{lat},{lng}"
        else:
            print(f"No se encontró la ciudad: {ciudad}")
            return None
    else:
        print("Error al obtener coordenadas:", res.status_code)
        return None

def obtener_datos_viaje(origen_coord, destino_coord, transporte):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen_coord, destino_coord],
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
        print("Respuesta:", response.text)
        return None

def main():
    print("== Medidor de distancia entre ciudades (Chile - Argentina) ==")
    while True:
        origen = input("Ingrese ciudad de origen (o 's' para salir): ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese ciudad de destino: ")
        print("Tipos de transporte disponibles: car, bike, foot")
        transporte = input("Ingrese medio de transporte: ")

        origen_coord = obtener_coordenadas(origen)
        destino_coord = obtener_coordenadas(destino)

        if origen_coord and destino_coord:
            ruta = obtener_datos_viaje(origen_coord, destino_coord, transporte)
            if ruta:
                distancia_km = ruta["paths"][0]["distance"] / 1000
                distancia_mi = distancia_km * 0.621371
                duracion = ruta["paths"][0]["time"] / (1000 * 60)
                narrativa = ruta["paths"][0]["instructions"]

                print(f"\nDistancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
                print(f"Duración estimada: {duracion:.1f} minutos")
                print("\nNarrativa del viaje:")
                for paso in narrativa:
                    print(f" - {paso['text']}")

if __name__ == "__main__":
    main()

