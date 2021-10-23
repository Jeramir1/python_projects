alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

storemessage = []
storemessageindex = []
encoded = []
def encrypt(text, shift):

    for letter in text:
        storemessage.append(letter)
        storemessageindex.append(alphabet.index(letter) + shift)
        original_position = alphabet.index(letter)
        encryptedindex = original_position + shift
        if encryptedindex > 25:
            encryptedindex = -1 + shift
        encoded.append(alphabet[encryptedindex])

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

if direction == 'encode':
    encrypt(text, shift)
    print(f"The encoded message is {''.join(encoded)}")
elif direction == 'decode':
    decrypt(text, shift)
    print(f"The encoded message is {''.join(decoded)}")
else:
    print("I didn't understand that, please try again use: decode or encode")