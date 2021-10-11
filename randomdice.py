import random
print("Welcome to the Dice Roll Generator")
number_of_dice = 1
try_again = 'y'
while try_again == 'y':
    number_of_dice = input("Select the number of dice you want to roll\n")
    while number_of_dice != 0:
        result_per_dice = random.randrange(1,7)
        print (f"Dice number {number_of_dice} - {result_per_dice}")
        number_of_dice = int(number_of_dice) - 1
    try_again = input("Try again? y, n \n")