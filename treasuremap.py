# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#convierte el primer digito en la primera posicion
columns = int(position[0]) -1
#convierte el 2do digito a la segunda posicion
rows = int(position[1]) -1
#reemplaza el tile por la bolsita del tesoro usando columns y rows de arriba.
map [rows][columns] = "💰"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")