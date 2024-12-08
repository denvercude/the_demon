from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY
from pydub import AudioSegment

elevenlabs_api_key = ELEVENLABS_API_KEY

def speak_text(text, pitch_factor):
    try:
        # Initialize ElevenLabs client
        client = ElevenLabs(api_key=elevenlabs_api_key)

        # Generate the TTS audio data using ElevenLabs
        audio_data_generator = client.generate(text=text, voice="A1ogBxJiby33RS5LScIs", model="eleven_monolingual_v1")
        
        # Collect all chunks from the generator into a single audio file
        audio_path = "response_original.mp3"
        with open(audio_path, "wb") as file:
            for chunk in audio_data_generator:
                file.write(chunk)

        # Load the generated audio using pydub
        audio = AudioSegment.from_file(audio_path)

        # Lower the pitch by changing the playback speed
        lowered_pitch_audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * pitch_factor)
        }).set_frame_rate(audio.frame_rate)

        # Create a whisper layer by high-passing and lowering the volume
        whisper_layer = lowered_pitch_audio.high_pass_filter(4000).apply_gain(-8)

        # Combine the main voice, whisper, and reverb layers
        demonic_voice = lowered_pitch_audio.overlay(whisper_layer)

        # Export the modified audio to response.mp3
        demonic_voice.export("response.mp3", format="mp3")

        return "response.mp3"
    except Exception as e:
        print(f"Error with TTS engine or audio processing: {e}")
        return None