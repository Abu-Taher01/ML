# Goal: Create a dictionary `user = {"id": 1}`. 
#       Try to access `user["email"]`. Then try to access it safely.

user = {"id" : 1}

# print(user["email"])
# This will raise a KeyError

print(user.get("email","Email not found"))