Overview
--------
the_demon is a Python-based voice interaction system that establishes a real-time conversation with ChatGPT, prompting it to roleplay as a funny, sarcastic demon. 
The system converts text responses into speech and dynamically visualizes the audio output using a bar graph that simulates a computer's mouth.
I made this after watching the movie Late Night with the Devil and is just a fun exploration of ChatGPT's API and figuring out audio visualization techniques.

Features
--------
- Real-time Voice Chat: Captures user speech input and responds with generated audio.
- Character Personality: ChatGPT is prompted to embody a sarcastic demon.
- Audio Visualization: Displays voice responses as a moving bar graph.
- Full-Screen Display: Runs an immersive interface using Pygame.
- Dynamic Sound Processing: Uses FFT analysis to synchronize visuals with audio intensity.

Tech
----
- Python
- Pygame (GUI and visualization)
- ChatGPT API (AI responses)
- ElevenLabs API
- Speech Recognition
- Text-to-Speech Engine
- NumPy & FFT Analysis
- Wave & Pygame Mixer

Demo
----

[![Watch the video](https://img.youtube.com/vi/wF3bQWRroZg/0.jpg)](https://www.youtube.com/watch?v=wF3bQWRroZg)

Installation and Setup
----------------------

Follow these steps to set up and run the speech module.

1. Prerequisites

Ensure the following are installed on your system:

    Python 3.7+
    pip (Python package installer)
    Microphone and Speaker (to capture and playback audio)
    Internet Connection (for API communication)

2. System Dependencies

This module requires ffmpeg for audio processing. For Linux, install it using:

sudo apt-get update
sudo apt-get install ffmpeg

OR their equivalents on macOS or Windows

3. Setting Up a Virtual Environment

    Navigate to the project root directory (where this README is located).

    Create a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate

    Manually Select: Python Interpreter to /venv/bin/python

4. Python Dependencies

    Navigate to the project root directory (where this README is located).

    Install dependencies by running:
    
    pip install -r requirements.txt

5. Environment Configuration

Create a .env file in the root project directory to store API keys. This file will allow the module to connect to OpenAI and ElevenLabs services.

    Create .env with the following content (replace with your actual keys):
    
    OPENAI_API_KEY=your_openai_api_key_here
    ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

