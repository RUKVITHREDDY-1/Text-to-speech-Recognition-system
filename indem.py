from gtts import gTTS
import os
file = open("draft.txt", "r").read().replace("\n", " ")
language = input('enter the language to be converted')
speech = gTTS(text = str(enter the file name to be converted), lang = language, slow = False)
speech.save("voice.mp3")
os.system("start voice.mp3")
