import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEFAULT_PERSONA = "Friendly"  # Default chatbot persona
