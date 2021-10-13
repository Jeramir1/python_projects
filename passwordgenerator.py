#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letterpack = []
symbolpack = []
numberpack = []

for letter in letters:
    if nr_letters != 0:
        letter_number= random.randint(0, 51)
        int_letter_number = int(letter_number)
        pass_char = (letters[int_letter_number])
        nr_letters -= 1
        letterpack.append(pass_char)
#print (letterpack)


for symbol in symbols:
    if nr_symbols != 0:
        symbol_number= random.randint(0, 8)
        int_symbol_number = int(symbol_number)
        pass_symbol = (symbols[int_symbol_number])
        nr_symbols -= 1
        symbolpack.append(pass_symbol)
#print (symbolpack)



for number in numbers:
    if nr_numbers != 0:
        number_number= random.randint(0, 9)
        int_number_number = int(number_number)
        pass_num = (numbers[int_number_number])
        nr_numbers -= 1
        numberpack.append(pass_num)
#print (numberpack)

pass_lr = (''.join(letterpack))
pass_sy = (''.join(symbolpack))
pass_nr = (''.join(numberpack))
password = pass_lr + pass_sy + pass_nr
print (f"Your generated password is \033[91m\033[1m \033[4m{password}\033[0m")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_password = list(password)
random.shuffle(list_password)
shuffled_password = ''.join(list_password)
print (f"Your shuffled generated password is \033[91m\033[1m \033[4m{shuffled_password}\033[0m")
