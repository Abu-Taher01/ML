# Goal: Make print(use) show "User: [Name]" instead of memory address.
# Deep Dive: Override __str__ (for end-users) and __repr__ (for developers/debugging).

class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True

    def __str__(self):
        return f"User: {self.username}"

    def __repr__(self):
        return f"User(username='{self.username}', is_active={self.is_active})" 

user1 = User("Mango")

print(user1)

print(repr(user1))
