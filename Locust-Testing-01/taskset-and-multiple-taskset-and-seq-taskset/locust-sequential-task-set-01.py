from locust import SequentialTaskSet, task, constant, HttpUser

class SeqTaskSet(SequentialTaskSet):

    @task
    def get_200(self):
        self.client.get("/200")
        print("Successfully getting 200")
    
    @task
    def get_500(self):
        self.client.get("/500")
        print("Successfully getting 500")

class TestUser01(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [SeqTaskSet]