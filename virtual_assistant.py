import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import pyjokes
import datetime
import wikipedia

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not hear your request. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return ""

if __name__ == '_main_':
    say("Hello, I am Jarvis A.I. How can I assist you?")

    while True:
        query = takeCommand().lower()
        sites = [["youtube","http://www.youtube.com"],["wikipedia","http://wikipedia.org"],["google","http://google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query:
                say(f"Opening {site[0]}....")
                webbrowser.open(site[1])
        if "exit" in query or "quit" in query:
            say("Goodbye!")
            break
        if 'play' in query:
            song = query.replace('play','')
            say('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            print(current_time)
            say('Current time is ' + current_time)
        elif 'who is' in query:
            person = query.replace('who is','')
            info = wikipedia.summary(person, 1)
            print(info)
            say(info)
        elif 'joke' in query:
            say(pyjokes.get_joke())
        elif 'control mouse' in query:
            import mouse_controller