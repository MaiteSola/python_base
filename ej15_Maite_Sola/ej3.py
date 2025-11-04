#Control de errores altura y anchura no puedan ser iguales
def dibujarRectangulo(altura,anchura):
       #Dibujar el rectángulo
    for _ in range(altura):
        print("*" * anchura)

def ejecutar():

    while(True):
        try: 
            altura = int(input("Introduce la altura: "))
            anchura = int(input("Introduce la anchura: "))

            if (altura <=0 or anchura <=0):
                print("Introduce números positivos.")
                continue
            
            if(altura == anchura):
                print("La altura y la anchura no pueden ser iguales")
                continue

            if(altura >=40 or anchura >=40):
                print("Por favor, no me hagas pintar tanto.")
                continue
            

            dibujarRectangulo(altura,anchura)
            break
        except ValueError:
            print("Introduce números.")

 
if __name__ == "__main__":
    ejecutar()



    