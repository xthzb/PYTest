import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 130) #速度
engine.setProperty('volume',0.6)    #音量

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def say(__input:str):
    engine.say(__input)
    engine.runAndWait()
    pass
