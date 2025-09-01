from qag_python_final_project_todoist.web_model.pages.application import app

from selene import browser, be, have


def test_creating_task(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.visible)


def test_completing_task(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    app.today_page.complete_task(task_id)
    app.today_page.go_to_completed_page()
    assert browser.element(f'[href*="{task_id}"]').should(be.visible)


def test_deleting_task(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    app.today_page.delete_task(task_id)
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.not_.visible)


def test_adding_comment(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    comment = "And this is a new comment!"
    app.today_page.add_comment(task_id, comment)
    assert browser.element('[class="note_content"]').should(have.text(comment))


def test_comment_icon_appearing(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    comment = "And this is a new comment!"

    app.today_page.add_comment(task_id, comment)
    app.today_page.close_task_pop_up()
    assert browser.element('[aria-label="1 comment"]').should(be.visible)


def test_task_added_to_inbox(setup_today_page):
    task_id = app.today_page.create_task("This is a new task!")
    app.today_page.go_to_inbox_page()
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.visible)
