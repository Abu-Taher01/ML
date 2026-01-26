# Goal: Prevent external code from changing user.password. 
# Deep Dive: Rename it to __password. Python performs **Name Mangling**(-> _user__password),
#            making it harder(though not impossible) to access from outside.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private variable
        self.is_active = True

    def get_password(self):
        return self.__password 
    
user1 = User("Mango", "OnlyInSummeR")

# Trying to access the private variable directly will raise an AttributeError
# print(user1.__password) 

print(user1.get_password())