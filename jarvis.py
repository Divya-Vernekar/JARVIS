import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to take voice input from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            speak("Listening timed out, please try again.")
            return "None"
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please say that again.")
            speak("Sorry, I did not understand that. Please say that again.")
            return "None"
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            speak("I am having trouble connecting to the speech recognition service.")
            return "None"
        return command.lower()

# Main function to handle different commands
def jarvis():
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = take_command()
        if command == "None":
            continue
        
        understood = False

        if 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
            understood = True
        
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")
            understood = True
        
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            understood = True
        
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            understood = True
        
        elif 'play music' in command:
            music_dir = 'C:\\Users\\YourUsername\\Music'  # Change this to your music directory
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
            understood = True
        
        elif 'stop' in command or 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        
        if not understood:
            speak("I didn't understand that. Please say it again.")

if __name__ == "__main__":
    jarvis()
