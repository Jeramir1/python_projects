import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

user_choice = input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors: ")
int_user_choice = int(user_choice)
if int_user_choice <= len(game):
    print (f"You chose: {(game[int_user_choice])}")

    computer_choice = random.randint(0,2)
    int_computer_choice = int(computer_choice)
    print("Thinking...")
    time.sleep(1)
    print (f"The Computer chose: {(game[int_computer_choice])}")
    #Draw scenarios
    if int_user_choice == int_computer_choice:
        print("Draw")

        
    #Rock Scenarios
    elif int_user_choice == 0 and int_computer_choice == 1:
        print("You Lose")
    elif int_user_choice == 0 and int_computer_choice == 2:
        print("You Win")
        
    #Paper Scenarios
    elif int_user_choice == 1 and int_computer_choice == 0:
        print("You Win")
    elif int_user_choice == 1 and int_computer_choice == 2:
        print("You Lose")

    #Scissor Scenarios
    elif int_user_choice == 2 and int_computer_choice == 0:
        print("You Lose")
    elif int_user_choice == 2 and int_computer_choice == 1:
        print("You Win")

#Catchall error
else:
    print("You typed an invalid entry!, you loose!")