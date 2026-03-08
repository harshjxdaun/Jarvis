import speech_recognition as sr
import webbrowser
import pyttsx3

try:
    import musicLibrary
    MUSIC_AVAILABLE = True
except ImportError:
    MUSIC_AVAILABLE = False
    print("Warning: musicLibrary module not found. Music commands will be disabled.")

recogniser = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    if "stop" in c.lower():
        speak("Goodbye! Shutting down.")
        return True  # Signal to stop the loop

    if "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif c.lower().startswith("play "):
        if not MUSIC_AVAILABLE:
            speak("Music library is not available.")
            return False
        song = " ".join(c.lower().split(" ")[1:])
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak(f"Sorry, I don't have {song} in my music library.")
    else:
        speak("Sorry, I didn't understand that command.")

    return False  # Keep running


if __name__ == "__main__":
    speak("Hii! I am Jarvis, a speaking Chatbot! Call me whenever you need me!")

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recogniser.listen(source, phrase_time_limit=5, timeout=5)

            command = recogniser.recognize_google(audio)
            print(f"Heard: {command}")

            if command.lower() == "jarvis":
                print("Jarvis Active")
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recogniser.listen(source, phrase_time_limit=10, timeout=10)

                command = recogniser.recognize_google(audio)
                print(f"Command: {command}")

                should_stop = processCommand(command)
                if should_stop:
                    print("Jarvis stopped.")
                    break  # Exit the loop

        except sr.WaitTimeoutError:
            print("Listening timed out, retrying...")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
