from qag_python_final_project_todoist.web_model.pages.application import app

from config import EMAIL, PASSWORD
from conftest import setup_landing_page
from selene import browser, have


def test_login_email(setup_landing_page):
    app.landing_page.go_to_login_page()
    app.login_page.login_email(EMAIL, PASSWORD)
    assert browser.element('[data-testid="large-header"]').should(have.text('Today'))