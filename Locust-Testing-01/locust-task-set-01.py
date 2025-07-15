from locust import TaskSet, task, constant

class TaskSetTest(TaskSet):
    
    @task
    def get_response_01(self):
        self.client.get("/200")
        print("Successfully sent request")
    
    @task 
    def get_response_02(self):
        self.client.get("/404")
        print("Successfully sent request-02")