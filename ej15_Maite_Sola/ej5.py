def dibujarHexagono(altura):
    contador = 1

    for i in range(altura):
        espacios = " " * (altura -i -1)
        estrellas = "*" * (altura + 2 * i)
        print(espacios + estrellas)

    for i in range(altura - 2, -1, -1):
        espacios = " " * (altura - i - 1)
        estrellas = "*" * (altura + 2 * i)
        print(espacios + estrellas)
        

def ejecutar():
    while(True):

        try: 
            altura = int(input("Introduce la altura: "))
            

            if(altura <=0):
                print("Introduce un número mayor a cero")
                continue
            if(altura >= 50):
                print("No me hagas pintar tanto")
                continue
            dibujarHexagono(altura)
            break
        except ValueError:
            print("Error. Introduce un número.")

if __name__ == "__main__":
    ejecutar() 


