# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet(name): # 3 aqui le ponemos que la funcion va a tomar un argumento llamado name
    print(f"Good morning {name}") # 4  y aqui le estamos inyectando el name de la variable que pedimos en el paso 1
    print("Welcome to the function tutorial")
    print("This function prints 3 lines of code")

name = input("What is your name?") # 1 aqui tenemos el input con la variable
greet(name) # 2 aqui le estamos pasando la variable a la funcion

#el parameter es la el nombre de la data que le vamos a pasar a la funcion, por ejemplo: def function(parameter) y el argument es en si el valor que esta en ese parameter,en name era el nombre


def greet_with(name, location):
    print (f"Hello {name}")
    print (f"How is the weather like in {location}?")

name = input("What is your name? ")
location = input ("Where do you live?")

greet_with(name, location) #positional arguments son los que en python son basados en la posicion que tiene

#KWARGS!!!!
def kwargsfunc(a, b, c):
    print (f"Letter a = {a}")
    print (f"Letter b = {b}")
    print (f"letter c = {c}")

kwargsfunc(a = 1, c = 2, b = 3) #KEYWORD ARGUMENTS, se usan cuando quieres ser especifico en los argumentos y no importa que se revuelvan, comoquier alos va a interpretar de acuerdo a la definicion que le dimos como KWARG

greet_with(location = "Nowhere", name = "John Doe")
greet_with(name, location)