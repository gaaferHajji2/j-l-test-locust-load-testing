from locust import TaskSet, task, constant, HttpUser

class TaskSetTest(TaskSet):
    
    @task
    def get_response_01(self):
        response = self.client.get("/200")
        # print(f"response of 200 is: {response}")
        print("Successfully sent request")
    
    @task 
    def get_response_02(self):
        response = self.client.get("/404")
        # print(f"response of 404 is: {response}")
        print("Successfully sent request-02")

class LoadTestingWithTaskSet(HttpUser):
    tasks = [TaskSetTest]
    wait_time = constant(1)
    host = "https://http.cat"