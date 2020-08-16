import random
from locust import HttpUser, task, between
from itertools import count


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


class Visitor(HttpUser):
    _ids = count(0)
    abstract = True

    def get_tasks_count(self):
        tasks_count_http = self.client.get('/edu/tasks/count')
        return int(tasks_count_http.text)

    def select_task(self):
        tasks_count = self.get_tasks_count()
        item_id = random.randint(1, tasks_count)
        return item_id

    def send_task(self, value):
        task_id = self.select_task()
        page = self.client.get(f"/edu/tasks/{task_id}")
        csrftoken = page.cookies['csrftoken']

        self.client.post(
            f"/edu/tasks/{task_id}",
            {"action": value},
            headers={'X-CSRFToken': csrftoken}
        )

    @task(5)
    def index_page(self):
        self.client.get("/edu")
        self.client.get("/edu/tasks")

    @task(20)
    def submit_task(self):
        self.send_task(1)

    @task(10)
    def resolve_task(self):
        self.send_task(2)

    @task(10)
    def view_task(self):
        item_id = self.select_task()
        self.client.get(f"/edu/tasks/{item_id}")


class OrdinaryUser(Visitor):
    weight = 3
    wait_time = between(1, 9)

    def on_start(self):
        self.id = next(self._ids)
        # Поместить в __init__ родительского класса не получается:
        # __init__() takes 1 positional argument but 2 were given
        register = self.register().url
        if not register.endswith('complete/'):
            self.login()

    def login(self):
        page = self.client.get("/accounts/login/")
        csrftoken = page.cookies['csrftoken']

        response = self.client.post(
            "/accounts/login/",
            {
                "username": f"test_user_ordinary{self.id}",
                "password": "pass"
            },
            headers={'X-CSRFToken': csrftoken}
        )
        return response

    def register(self):
        page = self.client.get('/edu/accounts/register/')
        csrftoken = page.cookies['csrftoken']
        response = self.client.post(
            '/edu/accounts/register/',
            {
                "username": f"testuser{self.id}",
                "email": f"testuser{self.id}@example.com",
                "password1": "pass",
                "password2": "pass"
            },
            headers={'X-CSRFToken': csrftoken}
        )
        return response


class GuestUser(Visitor):
    weight = 5
    wait_time = between(1, 9)

    def on_start(self):
        self.id = next(self._ids)
        # Поместить в __init__ родительского класса не получается:
        # __init__() takes 1 positional argument but 2 were given
        self.client.get('/edu/guest/')

    def convert(self):
        page = self.client.get('/edu/convert/')
        csrftoken = page.cookies['csrftoken']
        response = self.client.post(
            '/edu/convert/',
            {
                "username": f"test_guest_user{self.id}",
                "password1": "pass",
                "password2": "pass"
            },
            headers={'X-CSRFToken': csrftoken}
        )
        return response

    def login(self):
        page = self.client.get("/accounts/login/")
        csrftoken = page.cookies['csrftoken']
        response = self.client.post(
            "/accounts/login/",
            {
                "username": f"test_user_guest{self.id}",
                "password": "pass"
            },
            headers={'X-CSRFToken': csrftoken}
        )
        return response

    @task
    def convert_or_login(self):
        page_url = self.convert().url
        if not page_url.endswith('done/'):
            self.login()
