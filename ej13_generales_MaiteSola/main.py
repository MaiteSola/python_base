import ej1
import ej2
import ej3
import ej4
import ej5
import ej6

def mostrar_menu():
    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Ecuaciones 2º grado")
    print("2. Adivinar el número")
    print("3. Orden especial")
    print("4. Números desplazados")
    print("5. Calcular MCD")
    print("6. Imprime pares")
    print("7. Finalizar programa")

def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Elige una opción del menú: "))
        except ValueError:
            print("Error: introduce un número válido.")
            continue  # Vuelve a mostrar el menú

        match opcion:
            case 1:
                ej1.ejecutar()
            case 2:
                ej2.adivinar_numero()
            case 3:
                num3 = ej3.leer_numeros()
                ej3.mostrar_orden_especial(num3)
            case 4:
                num4 = ej3.leer_numeros()
                ej4.mostrar_num_desplazados(num4)
            case 5:
                ej5.calcular_mcd()
            case 6:
                ej6.imprimeImpares()
            case 7:
                print("Programa finalizado")
                break
            case _:
                print("Opción no válida. Por favor, elige entre 1 y 7.")

if __name__ == "__main__":
    main()
