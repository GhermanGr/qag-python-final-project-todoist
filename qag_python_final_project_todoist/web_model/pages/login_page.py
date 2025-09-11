from config import ENDPOINT_LOGIN
from selene import browser, be
from time import sleep
import allure


class LoginPage:
    def __init__(self):
        pass

    @allure.step('Go directly to the login page')
    def open(self):
        with allure.step('Open browser at the landing page'):
            browser.open(ENDPOINT_LOGIN)

    @allure.step('Enter email and password to log in')
    def as_user(self, email: str, password: str):
        with allure.step('Locate the email input field'):
            browser.element('[type="email"]').should(be.visible)
        with allure.step('Enter the user email'):
            browser.element('[type="email"]').type(email)
        with allure.step('Enter the password'):
            browser.element('[type="password"]').type(password)
        with allure.step('Click the submit button'):
            browser.element('[type="submit"]').click()
        sleep(5)
        with allure.step('Confirm that the page finished loading'):
            browser.element('[data-testid="large-header"]').should(be.visible)
