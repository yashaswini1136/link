import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {date}")

def search_web(query):
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    speak("Hello! I am your voice assistant.")
    
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        
        elif "time" in command:
            tell_time()
        
        elif "date" in command:
            tell_date()
        
        elif "search" in command:
            query = command.replace("search", "")
            search_web(query)
        
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
