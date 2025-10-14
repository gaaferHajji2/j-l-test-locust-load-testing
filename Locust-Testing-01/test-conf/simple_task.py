from locust import task, HttpUser, constant, events
import logging

logger = logging.getLogger('jloka_test_events')
logger.setLevel(logging.DEBUG)

@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    logger.info(f"All users spawn successfully with count: {user_count}")

def on_request_success(request_type, name, response_time, response_length, **kwargs):
    if kwargs.get("exception") is None:
        logger.info(f"Request succeeded: {request_type} {name} took {response_time}ms")
def on_request_failure(request_type, name, response_time, exception, **kwargs):
        logger.error(f"Request failed: {request_type} {name} took {response_time}ms with error {exception}")

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    # This event is fired when the Locust environment is initialized
    # We can listen for the request event and check for success or failure.
    events.request.add_listener(on_request_success)
    events.request.add_listener(on_request_failure)

@events.quitting.add_listener
def check_res(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.5:
        logger.error("We have many failures")
    else:
        logger.info("Failure Rate is low")

class SimpleTask(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.target = self.host

    @task
    def exist(self):
        response = self.client.get('/', name=self.target)
        # print(response.status_code)
    
    @task
    def notExist(self):
        response = self.client.get('/loka.html', name=self.target + '/notExist')
        # print(response.status_code)