#Test Commit Comments

import pyttsx3
#import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speakPrint(saying): # Function that was used to abstract the print and speak duplications
    print(saying)
    speak(saying)

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    speakPrint("Welcome Back Sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speakPrint("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speakPrint("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speakPrint("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speakPrint("Jarvis at your service sir, please tell me how may I help you. ")

def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speakPrint("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speakPrint("I'm fine sir, What about you?")

        elif "fine" in query:
            speakPrint("Glad to hear that sir!!")

        elif "good" in query:
            speakPrint("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speakPrint(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speakPrint("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speakPrint("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speakPrint("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speakPrint("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "offline" in query:
            quit()