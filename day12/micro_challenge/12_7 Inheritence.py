# Goal: Create Admin(User). Add a method delete_db() only for admin. 
# Deep Dive: The child class inherits all attributes of the parent.
#            it checks its own namespace first, then the parent's. this
#            follows the **MRO** (Method Resolution Order).

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

class Admin(User):
    def delete_db(self):
        print(f"Admin {self.username} deleted the database.")

admin1 = Admin("mango", "OnlyInSuMmeR")
admin1.login()
admin1.delete_db()

user1 = User("apple", "OnlyInWinTeR")
user1.login()

# so child can use own __init__ or parent's __init__?
# yes. if child has its own __init__, it uses that.
# then how the parent __init__ is called?
# use super() to call parent's __init__.

class SuperAdmin(Admin):
    def __init__(self, username, password, level):
        super().__init__(username, password)  # Call parent's __init__
        self.level = level

    def super_delete_db(self):
        print(f"SuperAdmin {self.username} with level {self.level} deleted the entire database.")

super_admin1 = SuperAdmin("supermango", "AllPowerful", 10)
super_admin1.login()
super_admin1.delete_db()
super_admin1.super_delete_db()
