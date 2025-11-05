def pedir_ciudades():
    n = int(input("¿Cuántas ciudades? "))
    ciudades = []
    for i in range(n):
        nombre = input(f"Ingrese el nombre de la ciudad {i+1}: ")
        ciudades.append(nombre)
    return ciudades

def pedir_distancias(ciudades):
    n = len(ciudades)
    # Crear matriz de distancias inicializada en 0
    distancias = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):  # Solo preguntar para j>i
            km = int(input(f"¿Distancia {ciudades[i]}-{ciudades[j]}? "))
            distancias[i][j] = km
            distancias[j][i] = km  # La distancia es simétrica
    return distancias

def pedir_itinerario(ciudades):
    m = int(input("¿Cuántas ciudades tiene el itinerario? "))
    itinerario = []
    for i in range(m):
        while True:
            ciudad = input(f"Ingrese ciudad {i+1} del itinerario: ")
            if ciudad in ciudades:
                itinerario.append(ciudad)
                break
            else:
                print("Ciudad no válida. Intenta de nuevo.")
    return itinerario

def kms(itinerario, ciudades, distancias):
    total = 0
    for i in range(len(itinerario)-1):
        c1 = ciudades.index(itinerario[i])
        c2 = ciudades.index(itinerario[i+1])
        total += distancias[c1][c2]
    return total


#Programa principal
def ejecutar():
    print("\n--- Módulo Distancias ---")
    ciudades = pedir_ciudades()
    distancias = pedir_distancias(ciudades)
    itinerario = pedir_itinerario(ciudades)
    total_kms = kms(itinerario, ciudades, distancias)
    print(f"\nLa distancia total del itinerario es: {total_kms} km")
