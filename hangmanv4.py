import os
import random

import hangman_art
import hangman_words

# list of words taken from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# logo and art taken from hangman_art.py
print (hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
guessed_letters = []
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear = lambda: os.system('clear')
    clear()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print (f"You already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            guessed_letters.append(guess)

    #Check if user is wrong.
    if guess not in guessed_letters:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print (f"Sorry, but {guess} is not in the word")
        guessed_letters.append(guess)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    #print (guessed_letters)
    #Import the stages from hangman_art.py.
    print(hangman_art.stages[lives])
print(f"the word was {chosen_word}")
