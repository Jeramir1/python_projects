programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}
# Retrieving information from a dictionary
print(programming_dictionary["Bug"])

#Adding information to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# print (programming_dictionary)

empty_list = []
empty_dictionary = {}

# whipe existing dictionary
# programming_dictionary={}
# print (programming_dictionary)

# edit a dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"] =  "Es un insecto"
# print (programming_dictionary["Bug"])

# loop throufh a dictionary
for key in programming_dictionary:
    print (key)
    print (programming_dictionary[key])
    
    