# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Groq API Key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file.")

# Optional default LLM settings
DEFAULT_MODEL = "llama-3.1-8b-instant"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TOP_P = 1
DEFAULT_TOP_K = None
DEFAULT_STOP_SEQUENCE = None
