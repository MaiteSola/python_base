# Imprime true o false en condicional

x = 2
print(x == 2) # imprime True
print(x == 3) # imprime False
print(x < 3) # imprime True

# booleanos

name="Maite"

if name == "John" or name == "Rick":
    print("Tu nombre es John o Rick.")
    pass
else:{
    print("Mal")
    }

# Verificar en un contenedor de objetos. Si john está en contenedor print.
name = "John"
if name in ["John", "Rick"]:
    print("Tu nombre es John o Rick.")

# Otro bloque
statement = False
another_statement = True
if statement is True:
    # hacer algo
    pass
elif another_statement is True: # else if
    # hacer otra cosa
    pass
else:
    # hacer una cosa diferente
    pass

# OPERADOR 'IS'
# "==" VS IS
x = [1,2,3]
y = [1,2,3]
print(x == y) # Imprime True
print(x is y) # Imprime False porque la x y la y no son lo mismo.


# NOT invierte la expresión
print(not False) # Imprime True
print((not False) == (False)) # Imprime False



