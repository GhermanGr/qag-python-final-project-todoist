from qag_python_final_project_todoist.web_model.pages.application import app
from selene import browser, be, have


def test_creating_task(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!")
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.visible)


def test_completing_task(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!2")
    app.today.complete_task(task_id)
    app.today.go_to_completed_page()
    assert browser.element(f'[href*="{task_id}"]').should(be.visible)


def test_deleting_task(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!")
    app.today.delete_task(task_id)
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.not_.visible)


def test_adding_comment(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!")
    comment = "And this is a new comment!"
    app.today.add_comment(task_id, comment)
    assert browser.element('[class="note_content"]').should(have.text(comment))


def test_comment_icon_appearing(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!")
    comment = "And this is a new comment!"

    app.today.add_comment(task_id, comment)
    app.today.close_task_pop_up()
    assert browser.element('[aria-label="1 comment"]').should(be.visible)


def test_task_added_to_inbox(
    delete_tasks, login
):
    task_id = app.today.create_task("This is a new task!")
    app.today.go_to_inbox_page()
    assert browser.element(f'[id="task-{task_id}-content"]').should(be.visible)
