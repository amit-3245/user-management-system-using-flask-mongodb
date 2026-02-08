from pymongo import MongoClient
from config import Config

# Create MongoDB client using URI from config
client = MongoClient(Config.MONGO_URI)

# Select database (database name URI se aayega)
db = client.get_database()

# Users collection
users_collection = db["users"]


def get_users_collection():
    """
    Return users collection from the database
    """
    return users_collection
