import random
print ("Welcome to the coin flipper")
ready = input ("Ready to flip a coin? y, n\n")
if ready == 'y':
  try_again = 'y'
  while try_again == 'y':
    number_of_coins = 1
    number_of_coins = input("How many coins you want to flip?\n")
    while number_of_coins != 0:
      result = random.randint(1,2)
      if result == 1:
        print(f"\033[92m For coin number {number_of_coins} you got \033[1m \033[4mTails\033[0m")
      else:
        print(f"\033[96m For coin number {number_of_coins} you got \033[1m \033[4mHeads\033[0m")
      number_of_coins = int(number_of_coins)-1
    
    try_again = input ("\033[0m Try again? y, n\n")











