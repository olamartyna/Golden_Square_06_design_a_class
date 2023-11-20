# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

class TaskTracker:
    def __init__(self):
        self.list = []

    def add_task(self, task):
        # task/s added to the list
        self.list.append(task)
        # nothing returned

    def list_of_tasks(self):
        # list of tasks retured 
        return self.list
        