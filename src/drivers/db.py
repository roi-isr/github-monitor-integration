import os
import logging
import sys

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
    return [{
        'id': str(pr_details['_id']),
        'state': pr_details['state'],
        'title': pr_details['title'],
        'username': pr_details['user']['login'],
        'userAvatarUrl': pr_details['user']['avatar_url'],
        'screenshotUrl': pr_details.get('screenshot_url', ''),
        'times': {
            'create': pr_details['created_at'],
            'update': pr_details['updated_at'],
            'close': pr_details['closed_at'],
        }
    } for pr_details in await cursor.to_list(length=100)]

