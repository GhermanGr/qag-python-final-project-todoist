from config import ENDPOINT_LOGIN
from selene import browser, be
from time import sleep


class LoginPage:
    def __init__(self):
        pass

    def open(self):
        browser.open(ENDPOINT_LOGIN)

    def as_user(self, email: str, password: str):
        browser.element('[type="email"]').should(be.visible)
        browser.element('[type="email"]').type(email)
        browser.element('[type="password"]').type(password)
        browser.element('[type="submit"]').click()
        sleep(5)
        browser.element('[data-testid="large-header"]').should(be.visible)
