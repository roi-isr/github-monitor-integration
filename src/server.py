from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from .drivers import db, selenium, firebase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_all_pull_requests():
    return jsonable_encoder(await db.get_all_pull_requests())


@app.post('/', status_code=status.HTTP_201_CREATED)
async def monitor_pull_request(request: Request, response: Response):
    github_action_details = await request.json()

    try:
        pull_request_details = github_action_details['pull_request']
    except KeyError:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {'message': 'No Pull Request data is provided in the payload'}

    if 'html_url' in pull_request_details.keys():
        screenshot_binary = selenium.get_website_screenshot_binary(url=pull_request_details['html_url'])
        screenshot_url = firebase.save_image(image_binary=screenshot_binary)

    await db.save_pull_request_log(
        {**pull_request_details, 'action': github_action_details['action'], 'screenshot_url': screenshot_url}
    )

    user = pull_request_details.get("user", {}).get("login", "N/A")
    return {'message': f'Pull Request was made by user {user} and was saved successfully'}
