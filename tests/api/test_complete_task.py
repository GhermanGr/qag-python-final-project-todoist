from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient
from http import HTTPStatus


def test_complete_task(tasks_client: TasksClient):
    got = tasks_client.complete_task()
    assert got.status_code == 204