from gtts import gTTS
import os

try_again = 'y'

while try_again == 'y':
    mytext = input( "Type anything here:")
    language = input("Select languange, en, es, fr, etc: ")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("TTSaudio.mp3")
    os.system("mpg321 TTSaudio.mp3")
    try_again = input("Try again? (y/n)")
