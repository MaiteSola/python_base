# Programa que pide dos números y calcula su máximo común divisor (MCD)
import math

def validar_input(numero_orden):
    while True:
        try:
            num = int(input(f"Introduce el {numero_orden}º número: "))
            return num
        except ValueError:
            print("Error: debes introducir un número entero válido.")

def calcular_mcd():
    print("=== PROGRAMA CALCULAR MCD ===")

    while True:
        print("\nCalculamos el Máximo Común Divisor")

        num1 = validar_input(1)
        num2 = validar_input(2)

        # Calculamos el MCD
        resultado = math.gcd(num1, num2)

        print(f"El resultado del MCD de {num1} y {num2} es: {resultado}")

        continuar = input("\n¿Quieres calcular otro MCD? s/n: ").lower()
        if continuar != "s":
            print("Actividad finalizada")
            break

# Ejecutamos solo si se llama directamente al script
if __name__ == "__main__":
    calcular_mcd()
