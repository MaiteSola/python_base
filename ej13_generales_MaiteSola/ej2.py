import random

def inputNum_val(mensaje="Introduce tu número: "):
    while True:
        try:
            num = int(input(mensaje))
            if 1 <= num <= 100:  # Validar que el número esté en el rango
                return num
            else:
                print("Error: El número debe estar entre 1 y 100.")
        except ValueError:
            print("Error: Debes introducir un número válido.")

def adivinar_numero():
    print("=== PROGRAMA ADIVINA EL NÚMERO ===")
    print("Adivina un número entre 1 y 100.")
    
    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0
        
        while True:
            num = inputNum_val("Introduce tu número: ")
            intentos += 1
            
            if num > numero_secreto:
                print("El número secreto es menor... sigue intentando.")
            elif num < numero_secreto:
                print("El número secreto es mayor... sigue intentando.")
            else:
                print(f"¡Has acertado el número {numero_secreto} en {intentos} intentos!")
                break  # Salir del bucle interno cuando se adivina el número
        
        # Preguntar si desea jugar de nuevo
        continuar = input("\n¿Quieres volver a jugar? (s/n): ").lower()
        if continuar != "s":
            print("Programa finalizado.")
            break
        print("\n=== Nuevo juego: Adivina el número entre 1 y 100 ===")

# Ejecutar el programa
if __name__ == "__main__":
    adivinar_numero()