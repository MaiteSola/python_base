#Almacenar una base de datos
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#Los diccionarios se pueden testear

libreria= {"John" : 123456789, "Jon" : 456789133}

for name, number in libreria.items():
    print("Phone number of %s is %d" % (name,number))


#eliminar un índice especifico
zerrendaEliminar = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
zerrendaEliminar.pop("Jill")
print(zerrendaEliminar)

#Ejercicio

lib = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

#lib["Jake"] = 444444444

lib.update({"Jake":444444444}) 

lib.pop("Jill")

if "Jake" in lib:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in lib:      
    print("Jill is not listed in the phonebook.")

 