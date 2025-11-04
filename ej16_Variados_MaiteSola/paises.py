#Programa que compara el número de países en común entre dos usuarios.
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    'Maite': {'Perú', 'Brasil', 'Portugal','Senegal'}
}

def validarInput(numero_orden):
    
    while(True):
        nom = input(f"Introduce el {numero_orden} nombre de la persona a comparar: ")

        if nom.capitalize() in paises:
            return nom.capitalize()
        else:
            print("Nombre no encontrado")

def cuantas_en_comun():
    #Vamos a comparar los países de esas personas.
    print("----PROGRAMA PAÍSES EN COMÚN----")
    print("Estos son los nombres que tenemos: ")
    for nombre in paises:
        print(f"- {nombre}")
        
    
    nom1 =validarInput("1")
    nom2 =validarInput("2")

    #Mirar si estamos comparando la misma persona

    if nom1 == nom2:
        print("No puedes comparar la misma persona")
        return
    
    #Recojo los países de cada uno así porque es un diccionario
    paisesNom1 = paises[nom1]
    paisesNom2 = paises[nom2]

    #La comparación se hace mediante intersección
    comunes = paisesNom1 & paisesNom2

    #Muestro los países de cada uno
    print(f"{nom1} Ha estado en: {', '.join(paisesNom1)}")
    print(f"{nom2} Ha estado en: {', '.join(paisesNom2)}")
    
    if comunes:
        if len(comunes)==1:
            print(f"Tienen {len(comunes)} país en común:  {', '.join(comunes)}")
        else:
            print(f"Tienen {len(comunes)} países en común:  {', '.join(comunes)}")
    else:
        print("No tienen países en común")
    
    
if __name__ == "__main__":
    cuantas_en_comun()