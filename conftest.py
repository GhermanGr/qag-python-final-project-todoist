import pytest
from selene import browser
from qag_python_final_project_todoist.web_model.pages.application import app
from config import EMAIL, PASSWORD, API_KEY
from doist_api_methods import delete_all_tasks
from qag_python_final_project_todoist.api_model.utils.client import Client
from qag_python_final_project_todoist.api_model.utils.configuration import Configuration
from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient

# API 
@pytest.fixture
def configuration(): 
    return Configuration(base_url="https://api.todoist.com", headers={"Authorization": f"Bearer {API_KEY}"})  # REST v1 API base URL

@pytest.fixture 
def client(configuration): 
    return Client(configuration=configuration)


@pytest.fixture
def tasks_client(client) -> Client: 
    return TasksClient(client=client)

# UI 
@pytest.fixture
def setup_landing_page():
    browser.config.browser_name = "chrome"
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = "https://www.todoist.com"
    browser.open("/")
    delete_all_tasks()
    yield
    browser.close()


@pytest.fixture
def setup_today_page():
    browser.config.browser_name = "chrome"
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = "https://www.todoist.com"
    browser.open()
    delete_all_tasks()
    app.login_page.open()
    app.login_page.login_email(EMAIL, PASSWORD)
    yield
    browser.close()

