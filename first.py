from unittest import result
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning")

    elif(hour>=12 and hour<=18):
        speak("good afternoon")
    
    else:
        speak("good evening!")

    
    speak("i am JARVIS sir. please tell how may i help you")


def takeCommand():
    #it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening----")
        r.pause_threshold= 1
        audio = r.listen(source)


    try:
        print("Recognizing---")
        query = r.recognize_google(audio, language="en-in")
        print("user said: ",query)

    except Exception as e:
        print(e)

        print("say that again please.....")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()               #converting users query into lower case

        # logic for executing task based on query
        if 'wikipedia' in query:                    #if wikipedia found in query then this block will be executed
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
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
            music_dir = "C:\Users\atulc\Music"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            print(My_joke)
            speak(My_joke)
        

        elif 'bye' in query:
            speak("no problem sir!...take care")
            break
        elif 'ok' in query:
            speak("have a nice day sir ")
            speak("bye")
            break

        

        
            



    


    
    