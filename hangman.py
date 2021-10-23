#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append('_')
print (display)




#TODO: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_len): #aqui estamos poniendo un RANGE para que nos aviente un numero de posicion en lugar de la letra con cada iteracion del for loop
        letter = chosen_word[position] #aqui le estamos inyectando la posicion a chosen word para que nos de esa letra, y le estamos asignando la variable letter
        if letter == guess:
            display[position] = letter #aqui le estamos diciendo que si la letra es igual al guess, entonces en DISPLAY nos vayamos a la posicion de arriba POSITION y la reemplazemos por la letra, y se vaya el _
    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(display)
    if "_" not in display:
        end_of_game = True
        print ("You Won!")