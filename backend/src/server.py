from fastapi import FastAPI, Request, Response, status
from .drivers import db, selenium

app = FastAPI()


@app.post('/', status_code=status.HTTP_201_CREATED)
async def monitor_pull_request(request: Request, response: Response):
    github_action_details = await request.json()

    try:
        pull_request_details = {**github_action_details['pull_request'], 'action': github_action_details['action']}
    except KeyError:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {'message': 'No Pull Request data is provided in the payload'}

    await db.save_pull_request_log(pull_request_details)

    if 'html_url' in pull_request_details.keys():
        selenium.save_website_screenshot(url=pull_request_details['html_url'], filename="test")

    user = pull_request_details.get("user", {}).get("login", "N/A")
    return {'message': f'Pull Request was made by user {user} and was saved successfully'}

