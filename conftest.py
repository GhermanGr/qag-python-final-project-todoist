import pytest
from selene import browser, have
from time import sleep
from qag_python_final_project_todoist.model.pages.application import app
from config import DOMAIN, ENDPOINT_LOGIN, EMAIL, PASSWORD, API_KEY
from doist_api_methods import delete_all_tasks



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
def setup_today_page():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open(DOMAIN)
    delete_all_tasks()
    app.login_page.open()
    app.login_page.login_email(EMAIL, PASSWORD)
    yield
    browser.close()
