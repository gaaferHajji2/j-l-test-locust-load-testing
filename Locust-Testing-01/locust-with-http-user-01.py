from locust import HttpUser, task, constant

class TestHttpUser(HttpUser):
    host = "https://example.com"

    wait_time = constant(1)

    @task
    def get_about_page(self):
        response = self.client.get("/")
        print("The Response Is: ", response.status_code)