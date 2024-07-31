import os
from dotenv import load_dotenv

def setup_environment():
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")