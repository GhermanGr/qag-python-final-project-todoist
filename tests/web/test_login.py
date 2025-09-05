from qag_python_final_project_todoist.web_model.pages.application import app

from config import EMAIL, PASSWORD
from selene import browser, have, be


def test_login_by_email(delete_tasks):
    app.landing.go_to_login_page()
    app.login.as_user(EMAIL, PASSWORD)
    assert browser.element('[data-testid="large-header"]').should(have.text("Today"))
