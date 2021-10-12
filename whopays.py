import random
import time
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #la funcion split hace que los elementos formen una lista automaticamente... MAGIA
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get total number of elements in the list - 1 because index starts at 0, not 1
name_index_number = (len(names) - 1)
#Select a random element from the list
winner = random.randint(0, name_index_number)
#Build exitement
print ("Thinking, please wait.") 
time.sleep(0.5)
print ("Thinking, please wait..") 
time.sleep(0.5)
print ("Thinking, please wait...") 
time.sleep(1)
#Print element with the result assigned by winner
print (f"Todays bill should be payed by {names[winner]}")

# ooo... podemos usar ramdon.choice y hacer todo en 1 linea
# print (f"Todays bill should be payed by {random.choice(names)}")