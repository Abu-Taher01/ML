# Goal: Try to decorate a function that takes arguments add(a,b) with a wrapper 
#       that takes note.

# Deep Dive: It crashes. The inner wrapper function MUST accept *args and **kwargs to be compitable 
#            with any target function signature.

def decorator(func):
    def inner(*args):
        print("Args", args)
        return func(*args)
    return inner

@decorator
def add(a,b):
    return a+b

print(add(2,3))