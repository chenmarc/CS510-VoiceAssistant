import pyttsx3
#import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

class VoiceAssistant:
    def __init__(self, name = "Jarvis"):
        self.engine = pyttsx3.init()
        self.name = name

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def speakPrint(self, saying):
        print(saying)
        self.speak(saying)

    def getTime(self):
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        self.speakPrint("The current time is: " + Time)

    def getDate(self): 
        day = int(datetime.datetime.now().day)
        month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)
        dateString = f"{day}/{month}/{year}"
        self.speakPrint("Todays date is: " + dateString)

    def wishMe(self):
        self.speakPrint("Welcome Back Sir!!")
        
        hour = datetime.datetime.now().hour
        if hour >= 4 and hour < 12:
            self.speakPrint("Good Morning Sir!!")
        elif hour >= 12 and hour < 16:
            self.speakPrint("Good Afternoon Sir!!")
        elif hour >= 16 and hour < 24:
            self.speakPrint("Good Evening Sir!!")
        else:
            self.speak("Good Night Sir, See You Tommorrow")

        self.speakPrint(f"{self.name} at your service sir, please tell me how may I help you. ")

    def screenshot(self):
        img = pyautogui.screenshot()
        img_path = os.path.expanduser("~\\Pictures\\JarvisSS.png")
        img.save(img_path)


    def takeCommand(self):
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
            self.speak("Please say that again")
            return "Try Again"

        return query

    def handleCommand(self, query):
        if "time" in query:
            self.getTime()

        elif "date" in query:
            self.getDate()

        elif "who are you" in query:
            self.speakPrint("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")

        elif "how are you" in query:
            self.speakPrint("I'm fine sir, What about you?")

        elif "fine" in query:
            self.speakPrint("Glad to hear that sir!!")

        elif "good" in query:
            self.speakPrint("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                self.speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                self.speakPrint(result)
            except:
                self.speak("Can't find this page sir, please ask something else")
        
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
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(song_dir, song))
            else:
                self.speakPrint("No sounds could be found.")

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                self.speakPrint("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = self.takeCommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                self.speakPrint("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            self.speak("What should I remember")
            data = self.takeCommand()
            self.speakPrint("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
    
        elif "do you remember anything" in query:
            try:
                with open("data.txt", "r") as remember_file:
                    data = remember_file.read()
                self.speakPrint("You told me to remember that " + data)
            except FileNotFoundError:
                self.speakPrint("You have not yet asked me to remember anything, please do so first.")

        elif "screenshot" in query:
            self.screenshot()

        elif "offline" in query:
            self.speakPrint("Going Offline, Sir. Goodbye!")
            quit()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.wishMe()
    while True:
        command = assistant.takeCommand()
        assistant.handleCommand(command)
