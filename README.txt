Installation and Setup

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

