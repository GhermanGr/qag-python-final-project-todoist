from qag_python_final_project_todoist.web_model.pages.application import app
import allure
from config import EMAIL, PASSWORD
from selene import browser, have, be
from time import sleep

@allure.step('Test logging in Todoist using user email and password')
def test_login_by_email(delete_tasks):
    sleep(20)
    app.landing.go_to_login_page()
    app.login.as_user(EMAIL, PASSWORD)
    with allure.step('Confirm that the Today page is open'):
        assert browser.element('[data-testid="large-header"]').should(have.text("Today"))
