from lib.TaskTracker import *

def test_task_tracker():
    task_tracker = TaskTracker()
    task_tracker.add_task('shopping')
    task_tracker.add_task('walk')
    task_tracker.add_task('call my friend')

    result = task_tracker.list_of_tasks()

    assert result == ['shopping', 'walk', 'call my friend']
    
