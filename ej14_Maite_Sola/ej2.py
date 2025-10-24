#Función que introduciendo un número de tres dígitos los ponga en orden inverso.
def ordenInverso(num):
    #El resto de %10 siempre me va a dar la ultima cifra
    n1 = num % 10 #Saco la cifra de las unidades
    #La segunda cifra es una divisón entera que descarta la última y reutilizamos el resto %10.
    n2 = (num // 10) %10 #saco la cifra de las decenas
    n3 = (num // 100) #Descarta las otras dos cifras
    return n1*100+n2*10+n3
   
def ejecutar():

   while True:
        try:
            num = int(input("Introduce un número de 3 dígitos: "))
            if 100 <= num <= 999:
               resultado = ordenInverso(num)
               print(f"Tu número invertido es: {resultado}")
               break
            else:
                print("Debe ser un número de tres dígitos")            
        except ValueError:
            print("Error: Introduce un número entero.")
  
        
if __name__ == "__main__":
    ejecutar()

