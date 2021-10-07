import pywhatkit
userText = input("Type anything to be converted to handwrite!")
pywhatkit.text_to_handwriting(userText, save_to="mytext", rgb=(0,0,0))