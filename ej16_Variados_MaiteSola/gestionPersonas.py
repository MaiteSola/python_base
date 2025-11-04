from datetime import date
import datetime
from typing import Counter
from personas import personas #para importar algo concreto

#Función para imprimir los nombres
def imprimir_nombres(personas):
    for (nombre,apellido, fecha) in personas:
        print(nombre)

meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}


#función para imprimir las fechas
def imprimir_fechas(personas):
    for (nombre,apellido,(dia,mes,ano)) in personas:
                
        print(f"{dia} de {meses[mes]} de {ano}")

#Función para contar el número de personas
def cuantas_personas(personas):
    
    print(f"El número de personas en la lista es: {len(personas)}")


#Función que retorne las personas que cumplen el mismo día que usuario.
#Validar input
def validarInputFecha():
    fecha_str = input("Introduce tu fecha de nacimiento (AAAA-MM-DD): ")
    while(True):
        try:
            #Python tiene esta función para validar la fecha
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            return fecha
        except ValueError:
            print("La fecha introducida no es válida.")

def devolver_fecha_coincidente(personas):
    fecha_usuario = validarInputFecha()
    dia_usuario = fecha_usuario.day
    mes_usuario = fecha_usuario.month

    coincidencias = []


    existe = False
    for (nombre, apellido, (dia,mes,_)) in personas:
        if dia == dia_usuario and mes == mes_usuario:
            coincidencias.append(f"{nombre} {apellido}")

    if coincidencias:
        print("Las personas que cumplen el mismo día que tú son: ")
        print(coincidencias)
    else:
        print("No hay nadie que cumpla el mismo día que tú.")

    return coincidencias

def nombre_mas_comun(personas):
    nombres = [nombre for (nombre, _, _) in personas]
    mas_comun = Counter(nombres).most_common(1)[0]
    print(f"El nombre más común es '{mas_comun[0]}' con {mas_comun[1]} ocurrencias.")
    return mas_comun
    

def ejecutar():
    print("\n--- PERSONAS ---")
    imprimir_nombres(personas)
    imprimir_fechas(personas)
    cuantas_personas(personas)
    devolver_fecha_coincidente(personas)
    nombre_mas_comun(personas)



if __name__ == "__main__":
    #Ejecutar
    ejecutar()
    
