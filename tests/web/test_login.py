from qag_python_final_project_todoist.web_model.pages.application import app
import allure
from config import EMAIL, PASSWORD
from selene import browser, have, be

@allure.step('Test logging in Todoist using user email and password')
def test_login_by_email(delete_tasks):
    with allure.step('Go from the landing page to the login page'):
        app.landing.go_to_login_page()
    app.login.as_user(EMAIL, PASSWORD)
    assert browser.element('[data-testid="large-header"]').should(have.text("Today"))
