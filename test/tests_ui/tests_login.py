from qag_python_final_project_todoist.model.pages.application import app

from config import EMAIL, PASSWORD
from conftest import setup_landing_page
from selene import browser, have


def test(setup_landing_page):
    app.landing_page.go_login_page()
    app.login_page.login_email(EMAIL, PASSWORD)
    assert browser.element('[data-testid="large-header"]').should(have.text('Today'))