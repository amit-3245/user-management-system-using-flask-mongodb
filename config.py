import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/user_managemen")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
