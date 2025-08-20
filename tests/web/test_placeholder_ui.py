from selene import browser
from time import sleep

def test_open_login_page():
    browser.open('https://www.todoist.com')
    sleep(5)