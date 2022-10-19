import pyttsx3
import speech_recognition as sr

import datetime

engine = pyttsx3.init('sapi5')  # voices lene ke liye
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("morning!")
    elif hour >= 12 and hour < 18:
        speak("afternoon!")
    else:
        speak("evening!")

    speak("Jarvis at your service!")


def takeCommand():
    # takes microphone input from user and returns string o/p

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # seconds of non speaking audio before a phase is complete
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("please repeat")
        return "None"  # none is string , not python none
    # recognise nhi hua to except block mei jaayega
    # take command audio microphone ki leke string me return krta h
    return query


if __name__ == "__main__":
    speak("hi kash how are you")
    wishMe()
    takeCommand()
