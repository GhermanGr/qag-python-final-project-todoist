from selene import browser


class LandingPage:
    def __init__(self):
        pass

    def go_to_login_page(self):
        browser.element('[href^="https://app.todoist.com/auth/login"]').click()
