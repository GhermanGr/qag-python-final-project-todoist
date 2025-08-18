import pytest
from selene import browser, have
from time import sleep
from qag_python_final_project_todoist.model.pages.application import app
from config import BASE_URL, ENDPOINT_LOGIN, EMAIL, PASSWORD, API_KEY
from doist_api_methods import delete_all_tasks



'''
FIXTURES
'''

@pytest.fixture
def setup_landing_page():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = 'https://www.todoist.com'
    browser.open('/')
    delete_all_tasks()
    yield
    browser.close()

@pytest.fixture
def setup_today_page():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = 'https://www.todoist.com'
    browser.open()
    delete_all_tasks()
    app.login_page.open()
    app.login_page.login_email(EMAIL, PASSWORD)
    yield
    browser.close()

@pytest.fixture
def setup_api_requests():
    browser.config.base_url = 'https://api.todoist.com'  # REST v1 API base URL
    yield