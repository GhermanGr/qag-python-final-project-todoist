from config import API_KEY
from todoist_api_python.api import TodoistAPI


def delete_all_tasks():
    api = TodoistAPI(API_KEY)
    all_tasks = api.get_tasks()
    for task_list in all_tasks:
        for task in task_list:
            api.delete_task(task.id)
            print(f"Deleted task: {task.id}")


def get_first_task_id():
    api = TodoistAPI(API_KEY)
    for task_page in api.get_tasks(limit=1):
        for task in task_page:
            print(task.id, task.content)
            return task.id
