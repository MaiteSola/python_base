# Programa que lee y valida 10 números introducidos por pantalla
# y los ordena de manera especial

def leer_numeros(cantidad=10):
    """Lee 'cantidad' números enteros desde el teclado y los devuelve en una lista"""
    numeros = []
    while len(numeros) < cantidad:
        try:
            num = int(input(f"Introduce el número {len(numeros)+1}: "))
            numeros.append(num)
        except ValueError:
            print("Error: Debes introducir un número entero.")
    return numeros

def mostrar_orden_especial(numeros):
    #Muestra la lista en orden especial: primero, último, segundo, penúltimo, ...
    nuevo_orden = []
    i, j = 0, len(numeros) - 1
    
    while i <= j:
        if i == j:
            nuevo_orden.append(numeros[i])
        else:
            nuevo_orden.append(numeros[i])
            nuevo_orden.append(numeros[j])
        i += 1
        j -= 1
    
    print("Orden especial:", nuevo_orden)

if __name__ == "__main__":
    print("=== PROGRAMA ORDEN ESPECIAL ===")
    numeros = leer_numeros()
    mostrar_orden_especial(numeros)
