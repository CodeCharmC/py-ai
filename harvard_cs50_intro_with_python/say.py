import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What do you want to say? ")
cowsay.dragon(this)
engine.say(this)
engine.runAndWait() 