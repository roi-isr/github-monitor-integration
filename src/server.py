import os

from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from .drivers import db, selenium, firebase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('FRONTEND_URL')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_all_pull_requests():
    pull_request_details = await db.get_all_pull_requests()
    return {
        'details': [{
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
            },
            'repositoryName': pr_details.get('repository_name')
        } for pr_details in pull_request_details]}


@app.post('/', status_code=status.HTTP_201_CREATED)
async def monitor_pull_request(request: Request, response: Response):
    github_action_details = await request.json()

    try:
        pull_request_details = github_action_details['pull_request']
    except KeyError:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {'message': 'No Pull Request data is provided in the payload'}

    screenshot_url = None
    if 'html_url' in pull_request_details.keys():
        screenshot_binary = selenium.get_website_screenshot_binary(url=pull_request_details['html_url'])
        screenshot_url = firebase.save_image(image_binary=screenshot_binary)

    await db.save_pull_request_log(
        {**pull_request_details, 'action': github_action_details['action'],
         'repository_name': github_action_details['repository']['name'], 'screenshot_url': screenshot_url or ''}
    )

    user = pull_request_details.get("user", {}).get("login", "N/A")
    return {'message': f'Pull Request was made by user {user} and was saved successfully'}
