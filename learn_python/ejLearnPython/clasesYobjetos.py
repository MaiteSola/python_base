#EjemploClaseBasica
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable) #Esto imprime bla

myobjecty= MyClass()

myobjecty.variable="yackity"
print(myobjecty.variable)
print(myobjectx.variable)

myobjectx.function() #esto imprime el mensaje


#INIT

#Es una función especial que se llama cuando la clase está siendo iniciada
#Se utiliza para asignar valores en una clase.

class NumberHolder:
    def __init__(self,number):
        self.number = number

        #init es el constructor
    
    def returnNumber(self):
        return self.number
    #Aquí es que queremos acceder al atributo number
    
var = NumberHolder(7)
print(var.returnNumber()) 

#ejercicio car

class Vehiculo:
    
    def __init__(self, nombre,tipo,color,valor):
        self.nombre=nombre
        self.tipo=tipo
        self.color=color
        self.valor = valor

    def descripcion(self):
        desc_str="%s is a %s , %s worth $%.2f." %(self.nombre,self.color,self.tipo,self.valor)
        return desc_str
    

car1 = Vehiculo('Fer','coche','rojo',60000.00)
car2 = Vehiculo('Jump','camioneta','azul',1000000)
  
print(car1.descripcion())
print(car2.descripcion())