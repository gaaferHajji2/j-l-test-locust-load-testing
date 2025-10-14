from locust import task, HttpUser, constant

class SimpleTask(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.target = self.host

    @task
    def exist(self):
        response = self.client.get('/', name=self.target)
        print(response.status_code)
    
    @task
    def notExist(self):
        response = self.client.get('/loka.html', name=self.target + '/notExist')
        print(response.status_code)