import ej1
import ej2
import ej3
import ej4
import ej5


while (True):
   
        print("\n ------MENÚ PRINCIPAL------")
        print("1. Números primos")
        print("2. Orden inverso")
        print("3. Dibujar rectángulo")
        print("4. Dibujar triángulo")
        print("5. Dibujar hexágono")
        print("6. Finalizar programa")
        try: 
            opcion = int(input("Elige una opción: "))

            match opcion:
                 
                 case 1:
                      ej1.ejecutar()
                      
                 case 2:
                      ej2.ejecutar()
                      
                 case 3:
                      ej3.ejecutar()
                      
                 case 4:
                      ej4.ejecutar()
                      
                 case 5:
                      ej5.ejecutar()
                                      
                 case 6:
                      ("Finalizando programa...")
                      break
                 case _:
                      print("No es una opción válida. Vuelve a escribir.")           

        except ValueError:
            print("Introduce una opción correcta")
            