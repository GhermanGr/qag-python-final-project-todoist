from selene import browser

class TodayPage():
    def __init__(self):
        pass

    def create_task(self):
        browser.element('[class="fc42413d _27c1200b _297575f4 c4a9b3ab c5d6948b"]').click()
        browser.element('[class="fc42413d _27c1200b _4e77e331 _77dba57f cdffd92b"]').click()
        browser.element('[class="is-empty is-editor-empty"]').type("This is my first task!")
        browser.element('[data-testid="task-editor-submit-button"]').click()

