# Goal: Create a class User. Ensure every user starts with is_active = True.
# Deep Dive: The __init__ method is the "constructor". Python calls it automatically 
#            immediately after memory allocation to initialize the objects state.

class User:
    def __init__(self):
        self.is_active = True

user1 = User()

print(user1.is_active)

user2 = User()

print(user2.is_active)