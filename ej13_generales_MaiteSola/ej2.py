#Programa que hace al usuario adivinar un número aleatorio indicando si el introducido es mayor o menor.
import random

def inputNum_val(mensaje="Introduce tu número: "):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Debes introducir un número válido.")

def adivinar_numero():
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
            print(f"¡Has acertado el número en {intentos} intentos!")
            continuar = input("¿Quieres volver a jugar? (s/n): ").lower()
            if continuar != "s":
                print("Programa finalizado.")
                break
            else:
                numero_secreto = random.randint(1, 100)
                intentos = 0
                print("\nNuevo juego: Adivina el número entre 1 y 100.")

# Ejecutar el programa
if __name__ =="__main__":
    adivinar_numero()
