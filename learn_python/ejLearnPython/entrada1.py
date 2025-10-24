# Imprime la entrada recibida desde stdin

from lib2to3.fixes import fix_input


print("Cuál es tu nombre?")
astring=input() # da Maite como entrada
print (astring)

#Después de recibir la entrada convertirla al tipo de dato que queremos.
print("Introduce un int: ")
num=int(input())
print("Se imprime")
print (num)
print("Introduce un float")
decimalnum=input()
print("Lo recoge como string")
#lo parsea
decimalnum=float(input())
print (decimalnum)


