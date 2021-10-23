#Aqui tenemos una lista con 12 elementos, pero estan revueltos 2 categorias, frutas y vegetales
#dirty_dozen =["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatores", "Celery", "Potatoes"]

#Lo que podemos hacer es hacer 2 listas, una para frutas y una para veggies y luego pegarlas en otra
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#Estariamos haciendo una NESTED LIST de 2 elemtnos (que en realidad esos 2 elementos son 2 listas completas independientes pero relacionadas) no lleva "" por que no son elementos strings
dirty_dozen = [fruits, vegetables]
print (dirty_dozen [1][1]) #aqui le estamos diciendo con el primer 1 que sea la 2da lista (0, 1) y con el 2do 1 le estamos diciendo que queremo el 2do elemento (kale)
