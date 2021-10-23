states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", 
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
                     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0]) #si ponemos el numero adentro de [] nos da el index que queremos imprmir
print(states_of_america[1])
print(states_of_america[2])
new_jersey = states_of_america[2]
print (new_jersey)
print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america[-3])
states_of_america[1] = "Pencilbania" #asi se pueden modificar los valores adentro de la lista, nomas se selecciona el index y se le asigna el nuevo valor como cualquier variable
print (states_of_america)
states_of_america.append("Angelaland")
print (states_of_america)
states_of_america.extend(["Piperland", "Ritaland", "Nanyland", "Chunkyland"]) #con extend se le puden agregar muchos valores, en forma de lista aqui mismo
print (states_of_america)
states_of_america.pop() #aqui se borra el elemento que especificamos, si no especificamos nada, entonces se borra el ultimo
print (states_of_america)
