from locust import User, task, constant

class Locust02Test(User):
    wait_time = constant(1)

    weight = 2

    @task
    def launch(self):
        print("Launching the URL")
    
    @task
    def search(self):
        print("Searching-01")

class Locust03Test(User):
    wait_time = constant(1)

    weight = 3

    @task
    def launch2(self):
        print("Launch the URL-02")
    
    @task
    def search2(self):
        print("Searching-02")