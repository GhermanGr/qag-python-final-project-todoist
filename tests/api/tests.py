from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient

def test_post_task(tasks_client: TasksClient):
    got, task_id = tasks_client.post_task()
    assert got.status_code == 200

def test_get_tasks(tasks_client: TasksClient):
    got = tasks_client.get_tasks()
    assert got.status_code == 204

def test_complete_task(tasks_client: TasksClient):
    got = tasks_client.complete_task()
    assert got.status_code == 204

def test_reopen_task(tasks_client: TasksClient):
    got = tasks_client.reopen_task()
    assert got.status_code == 204

def test_delete_task(tasks_client: TasksClient):
    got = tasks_client.delete_task()
    assert got.status_code == 204