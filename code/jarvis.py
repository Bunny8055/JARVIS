import pyttsx3
#module necessary to import for AI

import datetime
#module for time

import speech_recognition as sr
#module to recognize audio

import wikipedia
import webbrowser  #to open websites
import os

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
#'sapi5' to use inbuilt voices

#print(voices[0].id)

def speak(audio):              #to pronounce 
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    #print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir, I'm Jarvis. How may I help you..")    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'Password')
    server.sendmail('email', to, content)
    server.close()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)

    try:        #whenever there is error while listening
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'eng-ind')
        print("User said:",query)


    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query   

        
if __name__== "__main__":
    wishMe()
    while True:
    #if 1:
        query = takecommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open yoitube' in query:
            webbrowser.open('youtube.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"Sir, the time is {strTime}")

        elif 'open id' in query:
            path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
            os.startfile(path)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    

        elif 'quit' in query:
            exit()
