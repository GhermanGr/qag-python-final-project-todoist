import pytest
import json
from selene import browser, have
from time import sleep
from todoist_api_python.api import TodoistAPI
from config import DOMAIN, ENDPOINT_LOGIN, EMAIL, PASSWORD, API_KEY

from qag_python_final_project_todoist.model.pages.login_page import login_page



#@pytest.fixture
def setup_project():
    browser.open(DOMAIN)
    delete_all_tasks()
    login_page.open()
    login_page.login_email(EMAIL, PASSWORD)
    sleep(7)
    create_task_and_get_id()


def delete_all_tasks():
    api = TodoistAPI(API_KEY)
    all_tasks = api.get_tasks()
    for task_list in all_tasks:
        for task in task_list:
            api.delete_task(task.id)
            print(f"Deleted task: {task.id}")


def test_1():
    setup_project()

def create_task_and_get_id():
    browser.element('[class="fc42413d _27c1200b _297575f4 c4a9b3ab c5d6948b"]').click()
    browser.element('[class="fc42413d _27c1200b _4e77e331 _77dba57f cdffd92b"]').click()
    browser.element('[class="is-empty is-editor-empty"]').type("This is my first task!")
    browser.element('[data-testid="task-editor-submit-button"]').click()

    sleep(5)

def get_last_task_id():
    api = TodoistAPI(API_KEY)
    all_tasks = api.get_tasks()
    for task_list in all_tasks:
        if task_list:
            return task_list[0].id