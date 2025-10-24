# Bucles for
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    

# funcion range y xrange Python devuelve un iterador.

for x in range(5):
    print(x+1)
# Imprime los números 0,1,2,3,4
for x in range(5):
    print(x)


# Imprime 3,4,5
for x in range(3, 6):
    print(x)

# Imprime 3,5,7
for x in range(3, 8, 2):
    print(x)


# Bucles while
# Imprime 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # Esto es lo mismo que count = count + 1

# Sentencias break y continue
# 01234
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Imprime impares
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("ELSE")

# Uso del else en estas sentencias
# Si for o while falla se ejecuta la parte del else
count = 0
while(count <5):
    print(count)
    count += 1

else:
    print("El valor de count ya ha alcanzado el máximo que es %d" %(count))


    # ACTIVIDAD SIN TERMINAR

    numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number % 2 != 0:
        continue
    print(number)