# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.
class TaskTracker:
    def __init__(self):
        self.my_list = []

    def add_todo_task(self, list):
        for task in list:
            self.my_list.append(task)

    def remove_task_done(self, list):
        for task in list:
            self.my_list.remove(task)
    def remaining_list_of_tasks(self):
        pass
        return self.my_list

# task_tracker = TaskTracker()
# task_tracker.add_todo_task(["Finish Phase2","Buy groceries","Buy Table","Buy Chair"])
# task_tracker.remove_task_done(["Finish Phase2","Buy Table","Buy Chair"])
# print(task_tracker.remaining_list_of_tasks())