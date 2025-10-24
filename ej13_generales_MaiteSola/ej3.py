#Programa que lee y valida 10 números introducidos por pantalla y 1) los ordena de manera especial y 2) Desplaza una posición a la izquierda cada uno.
def leer_numeros(cantidad=10):
    numeros = []
    while len(numeros) < cantidad:
        try:
            num = int(input(f"Introduce el número {len(numeros)+1}: "))
            numeros.append(num)
        except ValueError:
            print("Error: Debes introducir un número entero.")
    return numeros


def mostrar_orden_especial(numeros):
    nuevo_orden = []
    #lo puedo hacer en manual o con un while con punteros inversos que se hace así:
    i, j = 0, len(numeros) - 1
    #la i marca el primero y la j marca que empieza desde el final.
    
    while i <= j:
        if i == j:
            nuevo_orden.append(numeros[i])
        else:
            nuevo_orden.append(numeros[i])
            nuevo_orden.append(numeros[j])
        i += 1
        j -= 1
    print("Orden especial:", nuevo_orden)

def mostrar_num_desplazados(numeros):
    
    nuevo_orden = []

    if len(numeros) == 0:
        print("Lista vacía")
        return

    # Guardo el primer num
    primer_num = numeros[0]

    # Recorro lista desde el número 1
    for i in range(1, len(numeros)):
        nuevo_orden.append(numeros[i])

    # Lo añado al final
    nuevo_orden.append(primer_num)

    print("Los números desplazados son:", nuevo_orden)
         
if __name__ == "__main__":
    #ejecuto
    numeros = leer_numeros()
    mostrar_orden_especial(numeros)
    mostrar_num_desplazados(numeros)

   

    
