from lib.TaskTracker import *

def test_task_tracker():
    task_tracker = TaskTracker()
    task_tracker.add_todo_task(['shopping','walk','call my friend'])
    task_tracker.remaining_list_of_tasks()
    task_tracker.remove_task_done(['shopping'])
    result = task_tracker.remaining_list_of_tasks()
    assert result == ['walk','call my friend']
   
