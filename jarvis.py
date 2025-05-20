import pyttsx3
import speech_recognition as sr
import pyaudio
import pywhatkit as pk
from datetime import date
from time import sleep
import random 

current_date = date.today()
# Format the date in text format
formatted_date = current_date.strftime("%d %B %Y")

recognizer = sr.Recognizer()
greeting =["Hello master Tanmay, Today is " + formatted_date,
    "Jarvis ready to roll, master!",
    "Another day, another creation, so let's start, master!",
    "Good day, master Tanmay! Let's make it productive.",
    "Greetings, master Tanmay. All systems are fully operational.",
    "Master Tanmay, today holds great potential. Shall we begin?",
    "Your assistant is online and ready to assist, master Tanmay.",
    "A wonderful day ahead, master! What's the mission?",
    "It's a pleasure to serve you, master Tanmay. Let's conquer the day.",
    "System check complete, master Tanmay. What's the agenda?",
    "I am here and at your service, master. Let’s innovate!",
    "Ready to explore, create, and achieve, master Tanmay!"
    ]


def search(google):
    pk.search(google)
    
def search_youtube(youtube):
    pk.playonyt(youtube)

def search_info(info):
   pk.info(info, lines=4)

def speak(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()
# Use the microphone as the source
greeting_number = random.randrange(0,11)
speak(greeting[greeting_number])
while True:
 with sr.Microphone() as source:
    speak("listening for command...")
    audio = recognizer.listen(source)  
    # Listen to the microphone inputs
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        speak("You said:"+text)
        print(text)
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
    except sr.RequestError:
        speak("Sorry, the service is unavailable.")
    
    if "stop system core" in text.lower():
       exit()
    if "wait for sometime" in text.lower():
       speak("Waiting for 30 seconds");sleep(30)
       speak("The wait is over sir")
    if "go to sleep" in text.lower():
       speak("Feeling tired already sir, Good night");sleep(300)
       speak("I feel refreshed sir, hope I woke up in time.")
    if "search on google" in text.lower():
       speak("Got it sir, what do you want to search?")
       with sr.Microphone() as source:
        audiot = recognizer.listen(source)  
        try:
            tosearch = recognizer.recognize_google(audiot)
            speak("You said:"+tosearch)
            print(tosearch)
            search(tosearch)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")
            pass
    if "search on youtube" in text.lower():
       speak("Got it sir, what do you want to search on youtube?")
       with sr.Microphone() as source:
        audioy = recognizer.listen(source)  
        try:
            tosearchy = recognizer.recognize_google(audioy)
            speak("You said:"+tosearchy)
            print(tosearchy)
            search_youtube(tosearchy)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")
            pass
 
       