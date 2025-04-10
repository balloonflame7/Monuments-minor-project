
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Balloonflame7:jatin%40%230212@nobino-worm-gpt-ai.pnhvasg.mongodb.net/?retryWrites=true&w=majority&appName=Nobino-worm-gpt-ai"

client = MongoClient(MONGO_URI)

print("📦 Available Databases in MongoDB Atlas:")
for db_name in client.list_database_names():
    print(" -", db_name)
