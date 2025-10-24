#Programa que pidiendo los coeficientes de una ecuación de 2º grado con sus soluciones reales.
import math

def ecuacion(a,b,c):

    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("No existen soluciones reales.")
        return None
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Existe una única solución real: x = {x:.4f}") #para que acepte decimales
        return (x,)
    else:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        print(f"Existen dos soluciones reales: x1 = {x1:.4f}, x2 = {x2:.4f}")
        return (x1, x2)

def pedir_numero(mensaje="Introduce un número: "):
    while True:
        try:
            num = float(input(mensaje)) 
            return num
        except ValueError:
            print("Error: Debes introducir un número válido.")

def ejecutar():

    while True:
        print("Ecuaciones de segundo grado")
        coeficiente1 = pedir_numero("Introduce el coeficiente a: ")
        
        coeficiente2 = pedir_numero("Introduce el coeficiente b: ")

        coeficiente3 = pedir_numero("Introduce el coeficiente c: ")

        if (coeficiente1 == 0):
            print("El coeficiente a no puede ser 0.")
        else:
            ecuacion(coeficiente1,coeficiente2,coeficiente3)


        continuar = input("\n¿Quieres resolver otra ecuación? s/n:  ").lower()
        if continuar != "s":
            print("Programa finalizado")
            break
   
if __name__ == "__main__":
    ejecutar()