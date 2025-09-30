from locust import User, constant, task

class LocustMethods(User):
    def on_start(self):
        print("on_start executed")
    
    @task
    def task01(self):
        print("task01 started")
    
    @task
    def task02(self):
        print("task02 started")
    
    def on_stop(self):
        print("on_stop started")