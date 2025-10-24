# Formato de los bloques
# block_head:
#     1st block line
#     2nd block line
#     ...


# Las funciones se definen:
def my_function():
    print("Hello from my function")

my_function()

#Funciones con argumentos
def my_function_argumentos(username, greeting):
    print("Hello, %s, From My Function!!, I wish you %s"%(username,greeting))

my_function_argumentos("Maite","Buenos días")

#operar
def sum_two_numbers(num1,num2):
    return num1+num2
x= sum_two_numbers(2,3)
print(x)

#Ejercicio
def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s, is a benefit of functions" %(benefit)


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()