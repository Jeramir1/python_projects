#Write your code below this line 👇
#Write your code below this line 👇

def prime_checker(number):
    prime = True
    for digits in range(2, number):
        if number % digits == 0:
            if number % number == 0:
                print (f"Divisible by {digits}")
                prime = False
            else:
                print(f"Not divisible by {digits}")
                prime = True
                
    if prime == True:
        print ("Prime Number")
    elif prime == False:
        print("Not a prime number")
    '''
'''



n = int(input("Check this number: "))
prime_checker(number=n)




n = int(input("Check this number: "))
prime_checker(number=n)



