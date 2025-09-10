from qag_python_final_project_todoist.api_model.clients.post_task import post_task
from qag_python_final_project_todoist.api_model.utils.client import Client
from http import HTTPMethod
import httpx


class TasksClient:
    def __init__(self, client: Client):
        self.client = client

    def delete_task(self) -> httpx.Response:
        post_got, task_id = self.post_task()

        got = self.client.request(
            method=HTTPMethod.DELETE, url=f"/api/v1/tasks/{task_id}"
        )
        return got

    def get_tasks(self) -> httpx.Response:
        self.post_task()

        got = self.client.request(
            method=HTTPMethod.GET, url="/api/v1/tasks"
        )
        return got

    def post_task(self) -> httpx.Response:
        payload = {
            "content": "FUCK ME DAADDYYYY!!!",
            "due_string": "2025-08-19",
            "priority": 1,
            "project_id": "6cX2hP46f34W4WGW",
        }

        got = self.client.request(
            method=HTTPMethod.POST, url="/api/v1/tasks", json=payload
        )

        task_id = got.json().get("id")

        return got, task_id

    def complete_task(self) -> httpx.Response:
        post_got, task_id = self.post_task()

        got = self.client.request(
            method=HTTPMethod.POST, url=f"/api/v1/tasks/{task_id}/close"
        )
        return got

    def reopen_task(self) -> httpx.Response:
        post_got, task_id = self.post_task()

        self.client.request(
            method=HTTPMethod.POST, url=f"/api/v1/tasks/{task_id}/close"
        )

        got = self.client.request(
            method=HTTPMethod.POST, url=f"/api/v1/tasks/{task_id}/reopen"
        )
        return got