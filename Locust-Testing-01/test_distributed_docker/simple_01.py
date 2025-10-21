from locust import task, constant, HttpUser

class SimpleTask(HttpUser):
    wait_time = constant(1)
    host = "http://example.com"

    @task
    def get_home(self):
        self.client.get('/')