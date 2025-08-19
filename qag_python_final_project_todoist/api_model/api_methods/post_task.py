import requests
from selene import browser
from conftest import API_KEY

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "content": "jfsws12",
    "due_string": "2025-08-19",
    "priority": 1,
    "project_id":"6cX2hP46f34W4WGW"
}

def post_task():
    base_url = browser.config.base_url
    endpoint = f'/api/v1/tasks'
    full_url = base_url + endpoint

    response = requests.post(full_url, data=payload, headers=headers)

    print(f'Response {response.status_code}: {response.text}')

    return response