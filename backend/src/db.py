import os
import logging
import sys

from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

logging_handler = logging.StreamHandler(sys.stdout)
logging_handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(logging_handler)

mongo_client = os.getenv('MONGO_URL')
logging.info(mongo_client)


client = AsyncIOMotorClient(mongo_client)
db = client.app
github_log_collection = db.pull_request_logs


async def save_pull_request_log(pull_request_log: dict):
    result = await github_log_collection.insert_one(pull_request_log)
    return result.inserted_id
