1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.
class MusicTracker:
    def __init__(self):
        # defining list

    def add(self, param):
        # we are going to add parameter to the list

    def return_list(self):
        # returning the list

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

    def test_music_track():
        music_tracker = MusicTracker()
        # we are going to add three music tracks and we are expecting a return of 
        # a list with all of three tracks

Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.:
