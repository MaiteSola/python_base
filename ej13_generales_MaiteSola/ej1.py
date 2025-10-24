# Programa que pide los coeficientes de una ecuación de 2º grado
# y calcula sus soluciones reales
import math

def ecuacion(a, b, c):
    """
    Calcula las soluciones reales de la ecuación de segundo grado ax^2 + bx + c = 0.
    Imprime los resultados y devuelve una tupla con las soluciones.
    """
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("No existen soluciones reales.")
        return None
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Existe una única solución real: x = {x:.4f}")
        return (x,)
    else:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        print(f"Existen dos soluciones reales: x1 = {x1:.4f}, x2 = {x2:.4f}")
        return (x1, x2)

def pedir_numero(mensaje="Introduce un número: "):
    """Pide un número al usuario y valida que sea float"""
    while True:
        try:
            num = float(input(mensaje)) 
            return num
        except ValueError:
            print("Error: Debes introducir un número válido.")

def ejecutar():
    """Función principal para resolver ecuaciones de segundo grado"""
    print("=== PROGRAMA ECUACIONES DE SEGUNDO GRADO ===")

    while True:
        coeficiente1 = pedir_numero("Introduce el coeficiente a: ")
        coeficiente2 = pedir_numero("Introduce el coeficiente b: ")
        coeficiente3 = pedir_numero("Introduce el coeficiente c: ")

        if coeficiente1 == 0:
            print("El coeficiente a no puede ser 0.")
        else:
            ecuacion(coeficiente1, coeficiente2, coeficiente3)

        continuar = input("\n¿Quieres resolver otra ecuación? s/n: ").lower()
        if continuar != "s":
            print("Actividad finalizada")
            break

if __name__ == "__main__":
    ejecutar()
