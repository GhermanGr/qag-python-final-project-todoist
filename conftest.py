import pytest
from selene import browser, support
from config import API_KEY, EMAIL, PASSWORD
import allure_commons
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from qag_python_final_project_todoist.web_model.pages.application import app
from doist_api_methods import delete_all_tasks
from qag_python_final_project_todoist.api_model.utils.client import Client
from qag_python_final_project_todoist.api_model.utils.configuration import Configuration
from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient
import os
import tempfile
import shutil


# API
@pytest.fixture
def configuration():
    return Configuration(
        base_url="https://api.todoist.com",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )  # REST v1 API base URL


@pytest.fixture
def client(configuration):
    return Client(configuration=configuration)


@pytest.fixture
def tasks_client(client) -> Client:
    return TasksClient(client=client)


# UI
@pytest.fixture(autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(ChromeDriverManager().install())
    browser.config.driver = webdriver.Chrome(service=service, options=options)
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.base_url = "https://www.todoist.com"
    browser.open("/")

    yield

    browser.quit()
    try:
        shutil.rmtree(user_data_dir)
    except Exception as e:
        print(f"Failed to clean up user data directory {user_data_dir}: {e}")


@pytest.fixture
def delete_tasks():
    delete_all_tasks()
    yield


@pytest.fixture
def login(delete_tasks):
    app.login.open()
    app.login.as_user(EMAIL, PASSWORD)
    yield


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> None:
    if call.when == "call":
        test_name = item.name.replace("test_", "").replace("_", " ").capitalize()
        allure.dynamic.title(test_name)
