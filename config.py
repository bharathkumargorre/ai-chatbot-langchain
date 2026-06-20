import os
from dotenv import load_dotenv

load_dotenv()

# ======================
# API Configuration
# ======================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# ======================
# Streamlit Configuration
# ======================

PAGE_TITLE = "AI Chatbot"

PAGE_ICON = "🤖"

LAYOUT = "wide"

# ======================
# Default LLM Settings
# ======================

DEFAULT_MODEL = "llama-3.1-8b-instant"

DEFAULT_TEMPERATURE = 0.7

DEFAULT_MAX_TOKENS = 1024

# ======================
# Available Models
# ======================

MODELS = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
]