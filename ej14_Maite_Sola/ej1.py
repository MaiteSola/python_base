##Programa que pide al usuario un número de primos y el programa saca esa cantidad de números primos.
def primos_cercanos(n):
    primos = [] #Lista de primos
    numero = 2 #el primer número primo

    while len(primos) < n:
        es_primo = True
        for i in range(2, int(numero**0.5)+1): #Calculo la raíz cuadrada porque si un primo tiene un divisor mayor que su raíz cuadrada, tiene necesariamente un divisor menor que su raíz cuadrada.
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            primos.append(numero)
        numero+=1 

    return primos

#Pedir datos al usuario
def ejecutar():
    while True:  
        entrada = input("Introduce un entero: ")
        try: 
            num = int(entrada)
            break
        except ValueError:
            print("Error: Introduce un número entero. Inténtalo de nuevo.")
    primos = primos_cercanos(num)
    print(f"Los {num} primeros números primos son: {primos}")

if __name__ == "__main__":
    ejecutar()

