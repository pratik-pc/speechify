import pyttsx3


def speech(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.setProperty('rate', 150)
  engine.setProperty('volume', 1.0)
  engine.runAndWait()