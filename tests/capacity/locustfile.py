from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/api/classify")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
