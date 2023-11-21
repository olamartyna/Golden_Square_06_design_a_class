# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.
class TaskTracker:
    def __init__(self):
        self.my_list = []
    def add_todo_task(self,task):
        self.my_list.append(task)
    def list_of_tasks(self):
        return self.my_list
task_tracker = TaskTracker()
task_tracker.add_todo_task("Buy groceries")
task_tracker.add_todo_task("Finish Phase2")
print(task_tracker.list_of_tasks())
#==========================================================
# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.
class TaskTracker:
    def __init__(self):
        self.my_list = []
    def add_todo_task(self,task):
        self.my_list.append(task)
    def remove_task_done(self,task):
        x = self.my_list(task)
        del self.my_list[x]
    def remaining_list_of_tasks(self):
        return self.my_list
task_tracker = TaskTracker()
task_tracker.add_todo_task("Finish Phase2")
task_tracker.add_todo_task("Buy groceries")
task_tracker.add_todo_task("Buy Table")
task_tracker.add_todo_task("Buy Chair")
task_tracker.remove_task_done("Finish Phase2")
print(task_tracker.remaining_list_of_tasks())