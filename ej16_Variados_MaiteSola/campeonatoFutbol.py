resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}

def obtener_lista_equipos(resultados):
    equipos = []
    for eq1, eq2 in resultados.keys():
        for eq in (eq1, eq2):
            if eq not in equipos:
                equipos.append(eq)
    return equipos

# def obtener_lista_equipos(resultados):
#     equipos = set() #Set se utiliza para crear una lista de elementos no repetidos y ordenados de manera arbitraria
#     for eq1, eq2 in resultados.keys():
#         equipos.add(eq1)
#         equipos.add(eq2)
#     return list(equipos)

def validarInput(resultados):
    equipos = obtener_lista_equipos(resultados)
    while(True):
       
        equipo = input("Introduce un nombre de equipo: ")
        
        if equipo.capitalize() in equipos:
            return equipo.capitalize()
        else:
            print("Ese equipo no está en el diccionario")
        
def calcular_puntos(resultados):
    print("Calcular los puntos de un equipo")
    equipo = validarInput(resultados)
    puntos= 0

    for (local,visitante),(goles_local,goles_visitante) in resultados.items():

        if equipo == local:
            if goles_local>goles_visitante:
                puntos +=3
            if goles_local== goles_visitante:
                puntos +=1
        if equipo == visitante:
            if goles_visitante>goles_local:
                puntos +=3
            if goles_local == goles_visitante:
                puntos +=1
    
    return print(f"{equipo} tiene {puntos}")

#Total de goles que anotó menos goles que recibió
def diferencia_goles(resultados):
    print("Calcular la diferencia de goles")
    equipo = validarInput(resultados)
    golesMetidos = 0
    golesRecibidos = 0
    diferenciaGoles = 0

    for (local,visitante),(goles_local,goles_visitante) in resultados.items():
        if equipo == local:
            golesMetidos += goles_local
            golesRecibidos += goles_visitante
        if equipo == visitante:
            golesMetidos += goles_visitante
            golesRecibidos += goles_local

    diferenciaGoles = golesMetidos - golesRecibidos
    return print(f"{equipo} tiene una diferencia de goles de {diferenciaGoles}")
    
#Ordenadr los equipos por posiciones según puntos, difGoles y Goles anotados
def calcular_estadisticas(resultados):
    """Calcula puntos, goles a favor, en contra y diferencia de goles por equipo."""
    equipos = obtener_lista_equipos(resultados)
    
    # Diccionario con las estadísticas de cada equipo
    tabla = {eq: {'puntos': 0, 'goles_favor': 0, 'goles_contra': 0} for eq in equipos}

    for (local, visitante), (goles_local, goles_visitante) in resultados.items():
        # Goles a favor y en contra
        tabla[local]['goles_favor'] += goles_local
        tabla[local]['goles_contra'] += goles_visitante
        tabla[visitante]['goles_favor'] += goles_visitante
        tabla[visitante]['goles_contra'] += goles_local

        # Asignar puntos
        if goles_local > goles_visitante:
            tabla[local]['puntos'] += 3
        elif goles_local < goles_visitante:
            tabla[visitante]['puntos'] += 3
        else:
            tabla[local]['puntos'] += 1
            tabla[visitante]['puntos'] += 1

    # Calcular diferencia de goles
    for eq in tabla:
        tabla[eq]['diferencia'] = tabla[eq]['goles_favor'] - tabla[eq]['goles_contra']

    return tabla


def posiciones(resultados):
    """Devuelve la lista de equipos ordenados según las reglas dadas."""

    print("Lista de equipos por posiciones: ")
    tabla = calcular_estadisticas(resultados)

    # Ordenar los equipos según: puntos ↓, diferencia ↓, goles a favor ↓
    equipos_ordenados = sorted(
        tabla.keys(),
        key=lambda eq: (
            tabla[eq]['puntos'],
            tabla[eq]['diferencia'],
            tabla[eq]['goles_favor']
        ),
        reverse=True
    )

    return print(equipos_ordenados)

def ejecutar():
    """Función principal del módulo de campeonato."""
    print("\n--- CAMPEONATO DE FÚTBOL ---")
    print("Equipos:", obtener_lista_equipos(resultados))
    calcular_puntos(resultados)
    diferencia_goles(resultados)
    posiciones(resultados)

if __name__ == "__main__":
    #Ejecutar métodos
    ejecutar()
