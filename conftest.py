import pytest
from selene import browser, support
from config import API_KEY, EMAIL, PASSWORD
import allure_commons
from selenium import webdriver
import allure
from qag_python_final_project_todoist.web_model.pages.application import app
from selenium.webdriver.chrome.options import Options
from doist_api_methods import delete_all_tasks
from qag_python_final_project_todoist.api_model.utils.client import Client
from qag_python_final_project_todoist.api_model.utils.configuration import Configuration
from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient


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


    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "128.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    # }
    #
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    #     options=options)
    #
    # browser.config.driver = driver

    #options.add_argument("--headless")

    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.base_url = "https://www.todoist.com"
    browser.open("/")

    yield

    browser.quit()


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