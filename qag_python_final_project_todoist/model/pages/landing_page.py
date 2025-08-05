from conftest import DOMAIN, ENDPOINT_LOGIN, EMAIL, PASSWORD
from selene import browser
from time import sleep

class LandingPage():
    def __init__(self):
        pass

    def open(self):
        browser.open()