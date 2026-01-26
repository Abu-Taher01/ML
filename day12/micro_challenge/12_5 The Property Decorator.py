# Goal: Create a "fake" variable user.age that is calculated from birth year when accessed.
# Deep Dive: Use @prperty. It looks like a variable access,
#            but runs a method behind the scenes. This is **Encapsulation**.

class User:
    def __init__(self, username, birth_year):
        self.username = username
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = 2024
        return current_year - self.birth_year
    
user1 = User("mango",2003)

print(user1.age)