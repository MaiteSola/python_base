import ej1
import ej2
import ej3
import ej4
import ej5
import ej6



while (True):

    print("\n ------MENÚ PRINCIPAL------")
    print("1. Ecuaciones 2º grado")
    print("2. Bucles")
    print("3. Dibujar rectángulo")
    print("4. Dibujar triángulo")
    print("5. Dibujar hexágono")
    print("6. Finalizar programa")

    try:
        opcion = int(input("Elige una opción del menú: "))

        match opcion:

            case 1:
                ej1.ejecutar()
            case 2:
                ej2.adivinar_numero()
            case 3:
                numIntro= ej3.leer_numeros() #Recoge y valida números introducidos por consola
                ej3.mostrar_orden_especial(numIntro) #Saca orden de: 1,10,2,9...
                ej3.mostrar_num_desplazados(numIntro) #Saca num desplazados 1 a la izq.
                
            case _:
                print("No es una opción correcta")
    except ValueError:
        print("Introduce una opción correcta")

    continuar = input("¿Quieres volver al menú? s/n").lower()
    if continuar != "s":
        print("Programa finalizado")
        break