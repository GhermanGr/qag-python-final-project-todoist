from qag_python_final_project_todoist.api_model.utils.client import Client
from http import HTTPMethod
import httpx

class TasksClient(): 
    def __init__(self, client: Client): 
        self.client = client 

    def delete_task(self) -> httpx.Response:
        got = self.client.request(method=HTTPMethod.DELETE, url="/api/v1/tasks/6cgMM9m764p448cW")
        return got 
    

