# Programa que pide un caracter a reemplazar, una frase y un número de veces.

def verificar_caracter(caracter):
    return len(caracter) == 1

def verificar_frase(frase):
    return len(frase.strip()) > 0

def verificar_numero(n):
    return 1 <= n <= 10

def cambia(frase, diccionario, n=None):
    resultado = frase
    for clave, valor in diccionario.items():
        resultado = resultado.replace(clave, str(valor), n) if n else resultado.replace(clave, str(valor))
    return resultado

def ejecutar():
    # Paso 1: Crear diccionario
    diccionario = {}
    while True:
        clave = input("Introduce un carácter a reemplazar (o deja vacío para terminar): ")
        if clave == "":
            break
        if not verificar_caracter(clave):
            print("Debes introducir **un solo carácter**. Intenta de nuevo.")
            continue
        valor = input(f"Introduce el valor de reemplazo para '{clave}': ")
        if not verificar_caracter(valor):
            print("Debes introducir **un solo carácter** como reemplazo. Intenta de nuevo.")
            continue
        diccionario[clave] = valor

    if not diccionario:
        print("No se ingresaron caracteres para reemplazar. Saliendo...")
        return

    # Paso 2: Pedir frase
    while True:
        frase = input("Introduce una frase: ")
        if verificar_frase(frase):
            break
        print("Debes introducir una frase válida. Intenta de nuevo.")

    # Paso 3: Pedir número de reemplazos
    while True:
        try:
            n = int(input("Introduce un número de reemplazos por carácter (1-10): "))
            if verificar_numero(n):
                break
            print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número entero.")

    # Paso 4: Mostrar resultado
    resultado = cambia(frase, diccionario, n)
    print("\nFrase original: ", frase)
    print("Frase modificada:", resultado)
