import speech_recognition as sr

# Initialize the recognizer
try:
    recognizer = sr.Recognizer()
except Exception as e:
    print(f"Error initializing recognizer: {e}")
    exit(1)

def capture_speech():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None