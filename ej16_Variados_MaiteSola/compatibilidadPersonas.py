from personas import signos_compatibles
#Los he metido en esa clase

# Lista válida de signos zodiacales
signos_validos = {
    'aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo',
    'libra', 'escorpio', 'sagitario', 'capricornio', 'acuario', 'piscis'
}


#Función para crear una persona
def crear_persona():
    print("\n--- Crear una nueva persona ---")

    # Nombre
    while True:
        nombre = input("Nombre: ").strip().capitalize()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    # Género
    while True:
        genero = input("Género (M/F): ").strip().upper()
        if genero in ('M', 'F'):
            break
        print("Ingresa 'M' para masculino o 'F' para femenino.")

    # Edad
    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0 and edad < 120:
                break
            else:
                print("Ingresa una edad válida entre 1 y 120.")
        except ValueError:
            print("Debes ingresar un número entero para la edad.")

    # Música favorita
    while True:
        musica = input("Música favorita: ").strip().lower()
        if musica:
            break
        print("Ingresa un tipo de música (rock, pop, salsa, etc.)")

    # Signo zodiacal
    while True:
        signo = input("Signo zodiacal: ").strip().lower()
        if signo in signos_validos:
            break
        print("Signo inválido. Debe ser uno de los siguientes:")
        print(", ".join(sorted(signos_validos)))

    # Retornamos la tupla persona
    persona = (nombre, genero, edad, musica, signo)
    print(f"Persona creada: {persona}")
    return persona

def compatibles(p1,p2):
    nombre1,genero1,edad1,musica1,signo1 = p1
    nombre2,genero2,edad2,musica2,signo2 = p2

    #1 - Géneros opuestos

    if genero1 == genero2:
        return False

    #2 - Diferencia de edad
    if (edad1 - edad2) >= 10:
        return False

    #3 - Compatibilidad zodiacal(mujer, hombre)

    if genero1 == 'F' and genero2 == 'M':
        return (signo1,signo2) in signos_compatibles
    elif genero1 == 'M' and genero2 == 'F':
        return (signo2,signo1)in signos_compatibles
    else:
        return False


def ejecutar():
    persona1 = crear_persona()
    persona2 = crear_persona()
    if compatibles(persona1,persona2):
        print(f"{persona1} y {persona2} son compatibles")
    else:
        print(f"{persona1} y {persona2} no son compatibles")

if __name__ == "__main__":
    ejecutar()