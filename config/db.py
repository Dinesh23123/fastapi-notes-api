import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env for local development.
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
	raise ValueError("MONGO_URI is not set. Add it in your .env file.")

conn = MongoClient(MONGO_URI)