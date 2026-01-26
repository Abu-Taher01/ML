# Goal: Explain why def method(self) is required.
# Deep dive: Python passes the instance object as the first argument 
#            automatically. user.login() -> user.login(user).
#            Without self, the method doesn't know which user's data to access.

class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True

    def login(self):
        return f"{self.username} has logged in."

    def logout(self):
        return f"{self.username} has logged out."


user1 = User("Mango") # this is a User object with username "Mango"

# what is constructor?
# The constructor is the __init__ method in a class.
# It initializes the object's attributes when an instance is created.
# Example: In User class, __init__ initializes username and is_active.

# what is intance?
# An instance is a specific object created from a class.
# Example: user1 is an instance of the User class.

# what is object?
# An object is an instance of a class that contains data and behavior.
# Example: user1 is an object of the User class.

print(user1.login())