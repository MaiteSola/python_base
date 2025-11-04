#Programa que al introducir tu fecha de nacimiento te devuelve tu signo zodiacal.
#Diccionario
import datetime

signos = {
   'aries':       (( 3, 21), ( 4, 20)),
   'tauro':       (( 4, 21), ( 5, 21)),
   'geminis':     (( 5, 22), ( 6, 21)),
   'cancer':      (( 6, 22), ( 7, 23)),
   'leo':         (( 7, 24), ( 8, 23)),
   'virgo':       (( 8, 24), ( 9, 23)),
   'libra':       (( 9, 24), (10, 23)),
   'escorpio':    ((10, 24), (11, 22)),
   'sagitario':   ((11, 23), (12, 21)),
   'capricornio': ((12, 22), ( 1, 20)),
   'acuario':     (( 1, 21), ( 2, 19)),
   'piscis':      (( 2, 20), ( 3, 20)),
}

#Validación de fecha
def validarFecha():
    while(True):
        fecha_str = input("Introduce tu fecha de nacimiento (AAAA-MM-DD): ")

        try:
            #Python tiene esta función para validar la fecha
            fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")

            return fecha.date()
        except ValueError:
            print("La fecha introducida no es válida.")

def determinar_signo():

    print("----SIGNOS DEL ZODIACO----")
    fechaNac = validarFecha()
    dia= fechaNac.day
    mes = fechaNac.month

    #signoFechaNac = signos[fechaNac] Esto compararía las claves pero las claves son los signos asi que necesito un for

    for signo, ((mes_inicio, dia_inicio), (mes_fin, dia_fin)) in signos.items():
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            print(f"Tu signo es: {signo.capitalize()}")
            return
                       
    print("No se pudo determinar el signo")

if __name__ == "__main__":
    determinar_signo()

