from conftest import setup_api_requests
from jsonschema import validate
from qag_python_final_project_todoist.api_model.schemas.get_tasks_schema import GET_TASKS_SCHEMA
from qag_python_final_project_todoist.api_model.api_methods.post_task import post_task

def test_delete_task(setup_api_requests):
    response = post_task()
    assert response.status_code == 200
