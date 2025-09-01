from time import sleep

from selene import browser, by
from selenium.webdriver import Keys

from doist_api_methods import get_first_task_id


class TodayPage:
    def __init__(self):
        pass

    def create_task(self, task_name):
        browser.element('//button[.//span[normalize-space()="Add task"]]').click()
        browser.element('[aria-label="Task name"]').type(task_name)
        browser.element('[data-testid="task-editor-submit-button"]').click()
        sleep(
            1
        )  # Небольшой период ожидания позволяет убедиться, что задача успела создаться,
        # иначе есть вероятность место task_id получить None
        task_id = get_first_task_id()
        return task_id

    def complete_task(self, task_id):
        browser.element(f'[aria-describedby="task-{task_id}-content"]').click()
        sleep(
            60
        )  # Почему-то список выполненных заданий обновляется не сразу, нужно подождать
        # до наступления следующей минуты

    def add_comment(self, task_id, comment):
        browser.element(f'[id="task-{task_id}-content"]').click()
        browser.element('[data-testid="open-comment-editor-button"]').click()
        browser.element('[class="is-empty is-editor-empty"]').type(f"{comment}")
        browser.element('[data-track="comments|add_comment"]').click()

    def delete_task(self, task_id):
        browser.element(f'[id="task-{task_id}-content"]').hover()
        browser.element('[data-testid="more_menu"]').click()
        browser.element(by.text("Delete")).click()
        sleep(3)
        browser.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def close_task_pop_up(self):
        browser.element('[aria-label="Close task"]').click()

    def go_to_completed_page(self):
        browser.element('[aria-label="Completed"]').click()

    def go_to_inbox_page(self):
        browser.element('[aria-label^="Inbox"]').click()
