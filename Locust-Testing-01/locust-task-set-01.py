from locust import TaskSet, task, constant, HttpUser

class TaskSetTest(TaskSet):
    
    @task
    def get_response_01(self):
        self.client.get("/200")
        print("Successfully sent request")
    
    @task 
    def get_response_02(self):
        self.client.get("/404")
        print("Successfully sent request-02")

class LoadTestingWithTaskSet(HttpUser):
    tasks = [TaskSetTest]
    wait_time = constant(1)
    host = "https://http.cat"