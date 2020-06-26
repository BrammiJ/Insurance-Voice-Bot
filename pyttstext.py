import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print (voice)
    voice.name == 'Alex'
    engine.setProperty('voice', voice.id)
    break

engine.say('Hello World')
engine.runAndWait()