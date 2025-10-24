# Programa que desplaza una posición a la izquierda los números de una lista

def mostrar_num_desplazados(numeros):
    #"Desplaza los números de la lista una posición a la izquierda y muestra el resultado"
   
        if len(numeros) == 0:
            print("Lista vacía")
            return

        # Guardamos el primer número y desplazamos
        primer_num = numeros[0]
        nuevo_orden = numeros[1:] + [primer_num]

        print("Los números desplazados son:", nuevo_orden)

        
if __name__ == "__main__":
    print("=== PROGRAMA NÚMEROS DESPLAZADOS ===")
    
    # Para que este script funcione independiente, pedimos los números
    from ej3 import leer_numeros  # Si se ejecuta de manera independiente, importar o definir leer_numeros
    numeros = leer_numeros()
    
    mostrar_num_desplazados(numeros)
