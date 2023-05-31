import os
from datetime import datetime

from firebase_admin import credentials, initialize_app, storage

firebase_private_key_path = os.getenv('FIREBASE_PRIVATE_KEY_PATH')

cred = credentials.Certificate(firebase_private_key_path)
initialize_app(cred, {'storageBucket': 'github-monitor-integration.appspot.com'})


def save_image(image_binary: bytes):
    bucket = storage.bucket()
    current_timestamp = datetime.now().timestamp()
    blob = bucket.blob(f'screenshots/pull_requests/{current_timestamp}.png')
    blob.upload_from_string(image_binary, content_type='image/png')

    blob.make_public()
    return blob.public_url
