from locust import HttpUser, task, constant

class TestHttpUser(HttpUser):
    host = "https://example.com"

    wait_time = constant(1)

    @task
    def get_about_page(self):
        self.client.get("/about")
        print("Getting about success")