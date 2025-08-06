from config import DOMAIN, ENDPOINT_LOGIN, EMAIL, PASSWORD
from selene import browser
from time import sleep

class LoginPage():
    def __init__(self):
        pass

    def open(self):
        browser.open(DOMAIN + ENDPOINT_LOGIN)

    def login_email(self, email, password):
        browser.element('[type="email"]').type(email)
        browser.element('[type="password"]').type(password)
        browser.element('[type="submit"]').click()
        sleep(5)



login_page = LoginPage()
def test_test():
    login_page.open()
    login_page.login_email(EMAIL, PASSWORD)