alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
storemessage = []
storemessageindex = []
encoded = []
def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    for letter in text:
        storemessage.append(letter)
        storemessageindex.append(alphabet.index(letter) + shift)
        original_position = alphabet.index(letter)
        encryptedindex = original_position + shift
        if encryptedindex > 25:
            encryptedindex = -1 + shift
        encoded.append(alphabet[encryptedindex])



    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛 FIXED

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
decstoremessage = []
dedstoremessageindex = []
decoded = []
def decrypt(text, shift):
    
    for letter in text:
        decstoremessage.append(letter)
        dedstoremessageindex.append(alphabet.index(letter) - shift)
        original_position = alphabet.index(letter)
        encryptedindex = original_position - shift
        if encryptedindex  < 0:
            encryptedindex = 26 - shift
        decoded.append(alphabet[encryptedindex])




  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
    print(f"The encoded message is {''.join(encoded)}")
elif direction == 'decode':
    decrypt(text, shift)
    print(f"The encoded message is {''.join(decoded)}")
else:
    print("I didn't understand that, please try again decode or encode")