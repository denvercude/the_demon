import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys and other configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEFAULT_MODEL = "gpt-3.5-turbo"