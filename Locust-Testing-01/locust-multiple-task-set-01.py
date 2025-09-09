from locust import task, TaskSet, constant, HttpUser

class TaskSet01(TaskSet):

    @task
    def get_200(self):
        self.client.get("/200")
        print("Getting 200 Successfully")

class TaskSet02(TaskSet):
    
    @task
    def get_201(self):
        self.client.get("/201")
        print("Getting 201 Successfully")

class TestUser(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [TaskSet01, TaskSet02]