import os

API_ID    = os.environ.get("API_ID", "23801870")
API_HASH  = os.environ.get("API_HASH", "9645cfafdfc9be9a7a46fb4874992cf6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8156991393:AAErGESkJko3F_uMk-i4BJ1CtScdg7ENYOU") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
