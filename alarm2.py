import time
import datetime


def alarm():
    try:
        Name = input("Enter your name: ")
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print("Current Time is: ", current_time)
        Time1=input("Enter the hour (HH): ")
        Time2=input("Enter the minute (MM): ")
        Time=Time1+":"+Time2
        while True:
            Standard_time=datetime.datetime.now().strftime("%I:%M")
            time.sleep(1)
            if Time==Standard_time:
                count=0
                while count<=10:
                    count=count+1
                    # creating a engine for voice mode
                    engine=pyttsx3.init()
                    # setting the voice
                    engine.say("Wake up"+Name)
                    engine.runAndWait()
                print("Thankyou For using the Interface")
                break
    except Exception as e:
        print(e)
alarm()
