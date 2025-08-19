import requests
from selene import browser
from conftest import setup_api_requests, API_KEY
from jsonschema import validate
from qag_python_final_project_todoist.api_model.schemas.get_tasks_schema import GET_TASKS_SCHEMA

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_tasks():
    base_url = browser.config.base_url
    endpoint = "/api/v1/tasks"
    full_url = base_url + endpoint

    response = requests.get(full_url, headers=headers)
    print(f'Response {response.status_code}: {response.text}')

    body = response.json()

    tasks = response.json().get("results", [])
    print("Tasks:", tasks)
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Content: {task['content']}")
            task_id = task['id']
            print(f'The task id is {task_id}')
    else:
        print("No tasks exist.")

    return response, body

