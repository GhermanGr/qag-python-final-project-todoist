import pytest
import json
from selene import browser, have
from time import sleep
from todoist_api_python.api import TodoistAPI
from config import DOMAIN, ENDPOINT_LOGIN, EMAIL, PASSWORD, API_KEY

from qag_python_final_project_todoist.model.pages.application import app


'''
FIXTURES
'''

@pytest.fixture
def setup_landing_page():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open(DOMAIN)
    delete_all_tasks()
    yield
    browser.close()

@pytest.fixture
def setup_main_page():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open(DOMAIN)
    delete_all_tasks()
    app.login_page.open()
    app.login_page.login_email(EMAIL, PASSWORD)
    yield
    browser.close()


'''
METHODS THAT MODIFY TASKS, PROJECTS, COMMENTS, ETC.
'''

def delete_all_tasks():
    api = TodoistAPI(API_KEY)
    all_tasks = api.get_tasks()
    for task_list in all_tasks:
        for task in task_list:
            api.delete_task(task.id)
            print(f"Deleted task: {task.id}")



def get_last_task_id():
    api = TodoistAPI(API_KEY)
    all_tasks = api.get_tasks()
    for task_list in all_tasks:
        if task_list:
            return task_list[0].id