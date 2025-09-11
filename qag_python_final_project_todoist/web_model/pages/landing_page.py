from selene import browser
import allure


class LandingPage:
    def __init__(self):
        pass

    @allure.step('Go from the landing page to the login page')
    def go_to_login_page(self):
        with allure.step('Press the "Sign in" button on the landing page'):
            browser.element('[href^="https://app.todoist.com/auth/login"]').click()
