1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.
class TaskTracker():
    def __init__(self):
        self.list = []

    def add_task(self, task):
        # task/s added to the list
        # nothing returned

    def list_of_tasks(self):
        # list of tasks retured 

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.
# add few tasks to the list and check if the list is correctly appended


Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.:
