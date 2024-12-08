from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

elevenlabs_api_key = ELEVENLABS_API_KEY

def speak_text(text, pitch_factor):
    try:
        # Initialize ElevenLabs client
        client = ElevenLabs(api_key=elevenlabs_api_key)

        # Generate the TTS audio data using ElevenLabs
        audio_data_generator = client.generate(text=text, voice="A1ogBxJiby33RS5LScIs", model="eleven_monolingual_v1")
        
        # Collect all chunks from the generator and save to a file
        with open("response.mp3", "wb") as file:
            for chunk in audio_data_generator:
                file.write(chunk)
        
        return "response.mp3"
    except Exception as e:
        print(f"Error with TTS engine or audio processing: {e}")
        return None