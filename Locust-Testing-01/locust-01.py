from locust import User, task, constant

class Locust01Test(User):

    #Here We Wait 0.5s Between Each Request, Where User-Class
    # Represent The User Behavior Depending On @task-Decorator
    wait_time = constant(0.5)

    @task
    def hello(self):
        print("Hello, Locust World!")

    @task
    def baka_baka(self):
        print("Baka, Baka Load Testing With Locust")