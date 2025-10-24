# da dos enteros en la primera línea y más de dos enteros en la tercera línea
a, b = map(int, input().split()) # los das separados y esta linea los convierte a int y luego a un array de esos números : [3,7]
array = input().split() #aquí te pide otros números para hacer un array
sum = 0
for each in array:
    sum = sum + int(each) #los parsea a int aquí
print(a, b, sum)  # imprime los dos primeros enteros de la primera línea y la suma de los enteros de la segunda línea