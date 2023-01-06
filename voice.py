import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def sayName(name):
    engine.say(name)
    engine.runAndWait()