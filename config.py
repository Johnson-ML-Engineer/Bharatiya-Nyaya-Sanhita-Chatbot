import os
from dotenv import load_dotenv

GOOGLE_API_KEY = "AIzaSyBKzMLEIN6IoNFzpxJtrNH-c53Sx1DQzNU"
def setup_environment():
    load_dotenv()
    return GOOGLE_API_KEY
