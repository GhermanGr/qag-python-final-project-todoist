from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient
from http import HTTPStatus


def test_delete_task(tasks_client: TasksClient):
    got = tasks_client.delete_task()
    assert got.status_code == 204
