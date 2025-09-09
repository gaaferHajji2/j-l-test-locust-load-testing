from locust import task, TaskSet, HttpUser, constant

class TaskSet01(TaskSet):

    @task
    def get_200(self):
        self.client.get("/200")
        print("Successfully Getting 200");

    @task
    class TaskSet02(TaskSet):

        @task
        def get_201(self):
            self.client.get("/201")
            print("Successfully Getting 201");
            self.interrupt(reschedule=False)


class TestUser(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [TaskSet01]