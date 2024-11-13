import speech_recognition as sr

# Initialize the recognizer
try:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.5  # Increase this to allow longer pauses
    recognizer.dynamic_energy_threshold = False  # Disable dynamic threshold adjustment
    recognizer.energy_threshold = 400  # Adjust this based on your environment
except Exception as e:
    print(f"Error initializing recognizer: {e}")
    exit(1)

def capture_speech():
    with sr.Microphone() as source:
        # Adjust for ambient noise before starting
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10)
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