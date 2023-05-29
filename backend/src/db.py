import os

from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = os.getenv('MONGO_URL')
client = AsyncIOMotorClient(mongo_client)
db = client.app
github_log_collection = db.github_logs


async def save_github_log():
    await github_log_collection.insert_one