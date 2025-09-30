from locust import HttpUser, constant, task

class SimpleTask(HttpUser):
    wait_time = constant(1)

    @task
    def get_home_page(self):
        self.client.get("/")