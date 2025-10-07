from locust import User, task, constant, tag

class Locust01Test(User):

    #Here We Wait 0.5s Between Each Request, Where User-Class
    # Represent The User Behavior Depending On @task-Decorator
    wait_time = constant(0.5)

    @task
    @tag('simple-01', 'simple-02')
    def hello(self):
        print("Hello, Locust World!")

    @task
    def baka_baka(self):
        print("Baka, Baka Load Testing With Locust")