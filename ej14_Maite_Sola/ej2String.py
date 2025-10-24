def invertir_tres_digitos():
    while True:
        entrada = input("Introduce un número entero de tres dígitos: ")
        if entrada.isdigit() and len(entrada) == 3:
            numero_invertido = int(entrada[::-1])  #Se llama slicing e invierte el String.
            return numero_invertido
        else:
            print("Error: Debes introducir exactamente 3 dígitos.")

# Ejemplo de uso
resultado = invertir_tres_digitos()
print(f"El número invertido es: {resultado}")