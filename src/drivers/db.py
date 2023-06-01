import os

from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = os.getenv('MONGO_URL')

client = AsyncIOMotorClient(mongo_client)
db = client.app
github_log_collection = db.pull_request_logs


async def save_pull_request_log(pull_request_log: dict):
    result = await github_log_collection.insert_one(pull_request_log)
    return result.inserted_id


async def get_all_pull_requests():
    cursor = github_log_collection.find()
    return await cursor.to_list(length=1000)
