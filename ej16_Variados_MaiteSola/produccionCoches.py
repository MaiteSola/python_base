sedan = [

    ("Material",7,5,60),
    ("Personal",10,15,60),
    ("Impuestos",5,7,60),
    ("Transporte",2,2,60) 

]

camioneta = [
    ("Material", 8, 5, 40),
    ("Personal", 9, 15, 40),
    ("Impuestos", 3, 7, 40),
    ("Transporte", 3, 2, 40)
]

economico = [
    ("Material", 5, 5, 90),
    ("Personal", 7, 15, 90),
    ("Impuestos", 2, 7, 90),
    ("Transporte", 1, 2, 90)

]

def coste_produccion_coches():
    #Gestión Sedan
    print("===PROGRAMA PRODUCCIÓN COCHES===")
    print("El Sedan gasta semanalmante:")
    resultadoTotalSedan=0
    resultadoTotal=0
    for (nombre,ud,cost,prod) in sedan:
        resultado = ud*cost*prod
        resultadoTotalSedan +=resultado
        print(f"{nombre}: {resultado} euros")
    resultadoTotal += resultadoTotalSedan

    #Gestión camioneta
    
    resultadoTotalCamioneta=0
    print("La Camioneta gasta semanalmante:")
    for (nombre,ud,cost,prod) in camioneta:
        resultado = ud*cost*prod
        resultadoTotalCamioneta+= resultado
        print(f"{nombre}: {resultado} euros")
    
    resultadoTotal += resultadoTotalCamioneta
    

    #Gestión Económico
    resultadoTotalEconomico=0
    
    print("El Económico gasta semanalmante:")
    for (nombre,ud,cost,prod) in economico:
        resultado = ud*cost*prod
        resultadoTotalEconomico += resultado
        print(f"{nombre}: {resultado} euros")

    resultadoTotal += resultadoTotalEconomico

    print(f"El gasto del Sedan es: {resultadoTotalSedan}")
    print(f"El gasto de la camioneta es: {resultadoTotalCamioneta}")
    print(f"El gasto del Económico es: {resultadoTotalEconomico}")
    print(f"El gasto total es de: {resultadoTotal}")




def ejecutar():
    print("====PROGRAMA DE PRODUCCIÓN DE COCHES====")
    coste_produccion_coches()

if __name__ =="__main__":
    ejecutar()