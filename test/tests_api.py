import requests
from allure_commons._allure import step
from selene import browser, have, be
from todoist_api_python.api import TodoistAPI

api_token = "b711fbaef903af7904e3c4be357784de29c510a0"  # Replace with your actual token
api = TodoistAPI(api_token)
api.delete_task('6cX2mX64rH4hx7R4')

def test_a():
    api.add_comment(content='6cX2mX54pjJ3rXfW',task_id='6cX2mX54pjJ3rXfW')