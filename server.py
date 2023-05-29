import json
from datetime import datetime

from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/')
async def test(request: Request):
    body = await request.json()
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(f'data/test_res_{now}.json', 'w') as f:
        json.dump(body, f)
    print(body)
    return {}

