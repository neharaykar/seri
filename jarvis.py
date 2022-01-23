from typing import MutableSequence
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am seri ,please tell me how can I help you")
def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='F:\\TRIVENI DON DJ\\download'
            songs=os.listdir(music_dir)
            print(songs) 
            
            os.startfile(os.path.join(  music_dir,songs[7]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir,the time is {strTime}")
        elif 'open code' in query:
            code_path="C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(code_path)
            

