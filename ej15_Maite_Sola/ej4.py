def dibujarTriangulo(altura):
    contador=1
    for _ in range(altura):
        print("*" * contador)
        contador+=1

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

            dibujarTriangulo(altura)
            break
        except ValueError:
            print("Error. Introduce un número.")

if __name__ == "__main__":
    ejecutar()


