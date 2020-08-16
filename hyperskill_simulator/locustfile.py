import random
from locust import HttpUser, TaskSet, task, between


class AdminUser(HttpUser):
    weight = 1
    wait_time = between(1, 10)

    @task
    def add_task(self):
        response = self.client.get("/admin/educational_platform/prototypetask/add/")
        csrftoken = response.cookies['csrftoken']
        self.client.post(
            "/admin/educational_platform/prototypetask/add/",
            headers={'X-CSRFToken': csrftoken}
        )

    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("/admin/login/")
        csrftoken = response.cookies['csrftoken']
        self.client.post(
            "/admin/login/",
            {"username": "admin", "password": "pass"},
            headers={'X-CSRFToken': csrftoken}
        )


class TaskBrowsing(TaskSet):
    @task
    def index_page(self):
        self.client.get("/edu")
        self.client.get("/edu/tasks")

    @task(3)
    def view_task(self):
        tasks_count_http = self.client.get('/edu/tasks/count')
        tasks_count = int(tasks_count_http.text)
        item_id = random.randint(1, tasks_count)
        self.client.get(f"/edu/tasks/{item_id}")


class WebUser(HttpUser):
    weight = 5
    wait_time = between(1, 9)
    tasks = TaskBrowsing

    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("/accounts/login/")
        csrftoken = response.cookies['csrftoken']
        self.client.post(
            "/accounts/login/",
            {"username": "testuser", "password": "pass"},
            headers={'X-CSRFToken': csrftoken}
        )
