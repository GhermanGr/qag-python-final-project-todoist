import pytest
from selene import browser, support
from config import API_KEY, EMAIL, PASSWORD
import allure_commons
from selenium import webdriver
import allure
from qag_python_final_project_todoist.web_model.pages.application import app

from doist_api_methods import delete_all_tasks
from qag_python_final_project_todoist.api_model.utils.client import Client
from qag_python_final_project_todoist.api_model.utils.configuration import Configuration
from qag_python_final_project_todoist.api_model.clients.tasks import TasksClient

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser, support
import allure_commons

import logging
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selene import browser, support
from webdriver_manager.chrome import ChromeDriverManager
import allure_commons

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


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
    logger.debug("Starting browser_management fixture")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use webdriver-manager for macOS, system path for Jenkins
    if platform.system() == "Linux":
        chromedriver_path = "/usr/bin/chromedriver"
    else:
        chromedriver_path = ChromeDriverManager().install()

    service = Service(
        executable_path=chromedriver_path,
        log_path="chromedriver.log"
    )
    logger.debug("Initializing WebDriver")
    browser.config.driver = webdriver.Chrome(
        service=service, options=options, timeout=300
    )
    logger.debug("WebDriver initialized")
    browser.config.window_width = 1080
    browser.config.window_height = 1080
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.base_url = "https://www.todoist.com"
    logger.debug("Opening base URL")
    browser.open("/")
    yield
    logger.debug("Quitting browser")
    browser.quit()

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
