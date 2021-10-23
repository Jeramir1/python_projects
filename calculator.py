from calcart import logo




# Calculator

def add (n1, n2):
    return n1 + n2

# Substract
def substract (n1, n2):
    return n1 - n2

# Multiply
def multiply (n1, n2):
    return n1 * n2

# Divide
def divide (n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide,
}

def calculator():
    print (logo)
    num1 = float(input("Whats the first number? "))
    num2 = float(input("Whats the second number? "))

    print ("Select your operator:")
    for symbol in operations:
        print (symbol)
    operation_symbol = input("Pick an operation from the line above: ")

    calculation_fuction = operations[operation_symbol]
    answer = calculation_fuction(num1, num2)


    print(f"{num1} {operation_symbol} {num2} = {answer}")

    chain_operations = input("Do you want to chain operations?")

    try_again = False

    if chain_operations == "y":
        try_again = True
        num1 = answer
        
    else:
        calculator()
        print("k, bye")

    while try_again == True:
        new_answer = answer
        num3 = float(input("Input a new number"))
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_fuction = operations[operation_symbol]
        new_answer = calculation_fuction(num1, num3)
        print(f"{answer} {operation_symbol} {num3} = {new_answer}")

        chain_operations = input("Do you want to try again?")
        if chain_operations == "y":
            try_again = True
            new_answer = answer
        else:
            calculator()
            try_again = False
            
        
calculator()