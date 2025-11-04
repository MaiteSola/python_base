import paises;
import zodiaco;
import campeonatoFutbol;
import gestionPersonas;
import produccionCoches;
while (True):
   
        print("\n ------MENÚ PRINCIPAL------")
        print("1. Países")
        print("2. Orden inverso")
        print("3. Campeonato de fútbol")
        print("4. Personas")
        print("5. Conexión personas")
        print("6. Producción de coches")
        print("7. Contraseña")
        print("8. Distancias")
        print("9. Finalizar programa")
        try: 
            opcion = int(input("Elige una opción: "))

            match opcion:
                 
                 case 1:
                    paises.cuantas_en_comun()
                      
                 case 2:
                    zodiaco.determinar_signo()
                      
                 case 3:
                    campeonatoFutbol.ejecutar()           
                      
                 case 4:
                    gestionPersonas.ejecutar()
                 case 5:
                    produccionCoches.ejecutar()              
                 case 6:
                    print("Por hacer")
                 case 7:
                    print("Por hacer")  
                 case 8:
                    print("Por hacer")
                 case 9:
                    ("Finalizando programa...")
                    break
                 case _:
                    print("No es una opción válida. Vuelve a escribir.")           

        except ValueError:
            print("Introduce una opción correcta")
            