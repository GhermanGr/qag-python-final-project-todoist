# from qag_python_final_project_todoist.api_model.clients.post_task import post_task
from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient

# def test_post_task(setup_api_requests):
#     response = post_task()
#     assert response.status_code == 200

def test_post_task(tasks_client: TasksClient):
    got, task_id = tasks_client.post_task()
    assert got.status_code == 200