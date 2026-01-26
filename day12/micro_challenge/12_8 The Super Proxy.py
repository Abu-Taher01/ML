# Goal: Override __int__ in Admin, but still run the USer setup.
# Deep Dive: Use super().__init__(). This calls the parent method, ensuring base initialization
#            logic isn't lost.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

class Admin(User):
    def __init__(self, username, password, admin_level):
        super().__init__(username, password)  # Call parent's __init__
        self.admin_level = admin_level

    def delete_db(self):
        print(f"Admin {self.username} with level {self.admin_level} deleted the database.")

admin1 = Admin("mango", "OnlyInSuMmeR", 5)
admin1.login()
admin1.delete_db()

user1 = User("apple", "OnlyInWinTeR")
user1.login()

