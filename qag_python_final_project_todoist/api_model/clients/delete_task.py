
from config import API_KEY

headers = {"Authorization": f"Bearer {API_KEY}"}


def delete_task():
    base_url = browser.config.base_url
    endpoint = "/api/v1/tasks/6cgMM9m764p448cW"
    full_url = base_url + endpoint

    response = requests.delete(full_url, headers=headers)
    print(f"Response {response.status_code}: {response.text}")

    return response
