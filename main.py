import speech_recognition as sr
import pyttsx3 as d
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes

x = sr.Recognizer()
y = d.init()
p = y.getProperty("voices")
y.setProperty("voice", p[1].id)

def time():
    c = datetime.now()
    g = c.strftime("%H")
    if 4 <= int(g) < 12:
        return "Good morning"
    elif 12 <= int(g) < 16:
        return "Good noon"
    elif 16 <= int(g) < 18:
        return "Good afternoon"
    elif 18 <= int(g) < 21:
        return "Good evening"
    else:
        return "Good night"





def repeat(text):
    y.say(text)
    y.runAndWait()

repeat(f"{time()}  daddy. I am siri. How can I help you?")



def take():
    try:
        with sr.Microphone() as c:
            print("listening.....")
            v = x.listen(c)
            t = x.recognize_google(v)
            t = t.lower()
            if "siri" in t:
                t = t.replace("siri", "")
                print(t)

    except:
        t = "ask somthing"
    return t


def main_job():
    infor = take()
    if "play" in infor:
        infor = infor.replace("play", "")
        repeat("playing " + infor)
        pywhatkit.playonyt(infor)
    elif "time" in infor:
        time = datetime.now().strftime("%I:%M %p")
        repeat("current time is" + time)
    elif "who" in infor:
        t = wikipedia.summary(infor, 1)
        repeat(t)
    elif "joke" in infor:
        t = pyjokes.get_joke()
        repeat(t)
    else:
        repeat("i did not understand what you said")


while True:
    main_job()
