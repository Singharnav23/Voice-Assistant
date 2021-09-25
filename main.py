import pyttsx3 as p
import speech_recognition as sr
import pyjokes
import datetime
from YT_auto import music
from selenium_web import *
from News import *
from weather import *
from Music import song
import randfacts

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        return "Good Morning"
    elif 12 <= hour < 16:
        return "Good Afternoon"
    else:
        return "Good Evening"


today_date = datetime.datetime.now()

r = sr.Recognizer()

speak("Hello sir, " + wishme() + ", i'm your voice assistant. ")
speak("Temperature in new delhi is ," + str(temp()) + "degree celsius" + " and with " + str(des()))

speak("what can i do for you")
'''
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print('Listening...')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("i am also having a good day sir ")

speak("what can i do for you??")
'''
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which vedio ??")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        speak("Playing {} on youtube".format(vid))
        print("Playing {} on youtube".format(vid))
        assist = music()
        assist.play(vid)

elif "news" in text2:
    speak("Sure sir, i will read news for you")
    print("Sure sir, i will read news for you")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "songs" or "song" or "music" in text2:
    speak("you want me to play which song ??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        mus = r.recognize_google(audio)
        speak("Playing {} on youtube music".format(mus))
        print("Playing {} on youtube music".format(mus))
        assist = song()
        assist.play(mus)

elif "fact" or "facts" in text2:
    speak("Sure sir, did you know")
    x = randfacts.get_fact()
    print(x)
    speak(x)

elif "joke" or "jokes" in text2:
    speak("Sure sir, get ready for some chuckles")
    arr = pyjokes.get_jokes()
    print(arr)
    speak(arr)
