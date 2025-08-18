import requests
from selene import browser
from conftest import setup_api_requests, API_KEY
from jsonschema import validate
from schemas.get_tasks_schema import GET_TASKS_SCHEMA

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def test_get_tasks(setup_api_requests):
    base_url = browser.config.base_url
    endpoint = "/api/v1/tasks"
    full_url = base_url + endpoint

    response = requests.get(full_url, headers=headers)
    print(f'Response {response.status_code}: {response.text}')
    assert response.status_code == 200

    tasks = response.json().get("results", [])
    print("Tasks:", tasks)
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Content: {task['content']}")
    else:
        print("No tasks exist.")

    body = response.json()
    validate(body, GET_TASKS_SCHEMA)