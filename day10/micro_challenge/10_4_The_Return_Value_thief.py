# Goal: Write ba decorator that forgets to return func(*args). Print the result of the decorated
#       function.

# Deep Dive: It prints None. A wrapper must explicity capture and return the result of the original function,
#            otherwise the data is lost inside the wrapper scope.

def decorator(func):
    def inner(*args):
        print("Args", args)
        func(*args)
    return inner

@decorator
def add(a,b):
    return a+b

print(add(2,3))