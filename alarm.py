import time
import datetime
import pyttsx3
import pyaudio
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)


def speak(audio): 
	engine.say(audio) 
	engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def alarm():
    try:
        speak("Enter your name: ")
        Name = takeCommand()
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print("Current Time is: ", current_time)
        print("Enter the hour (HH):")
        speak("Enter the hour")
        Time1=takeCommand()
        print("Enter the minute (MM):")
        speak("Enter the minute")
        Time2=takeCommand()
        Time=Time1+":"+Time2
        while True:
            Standard_time=datetime.datetime.now().strftime("%I:%M")
            time.sleep(1)
            if Time==Standard_time:
                count=0
                while count<=10:
                    count=count+1
                    speak("Wake up"+Name)
                print("Thankyou For using the Interface")
                break
    except Exception as e:
        print(e)
alarm()
