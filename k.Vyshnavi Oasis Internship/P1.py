import subprocess
import speech_recognition as sr
import webbrowser

def open_browser(search_term):
    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.open(url)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry could not recognize what you said")
            return listen()

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        text = listen()
        print("You said:", text)

        if "open browser" in text:
            talk("What would you like to search for?")
            search_term = listen()
            open_browser(search_term)

if __name__ == "__main__":
    main()
