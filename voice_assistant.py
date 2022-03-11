import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 175.85)

volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)

'''
engine.say("Hi Deepak\nI'm natasha\tyour voice assistant")
engine.runAndWait()


engine.say("Enter any of the above mentioned options")
engine.runAndWait()
'''


def reply(rep):
    engine.say(rep)
    engine.runAndWait()