#6. Escriba una función que sume los n primeros números impares.
#Programa que sume los "n" primeros números impares.

def validarNum():
    while(True):
        try:
            num = int(input("Introduce el número de impares que quieres imprimir:  "))
            return num
        except ValueError:
            print("Error. Introduce un número entero.")

def imprimeImpares():
    print("===PROGRAMA IMPARES===")
    while(True):
        num = validarNum()
        contador=-1
        for i in range(0, num):
            contador +=2
            print(contador)
        continuar = input("\n¿Quieres volver a calcular impares? s/n:  ").lower()
        if continuar != "s":
            print("Actividad finalizada")
            break

if __name__ == "__main__":
    imprimeImpares()