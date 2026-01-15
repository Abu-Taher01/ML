# Goal: Apply the wrapper using the @decorator syntax. 

# Deep dive: The @ symbol is "Syntactic Sugar". At compile time, Python reads 
#            this and automatically performs the re-assignment func = decorator(func).

def decorator(func):
    def wrapper():
        print("pre")
        func()
        print("post")
    return wrapper

@decorator
def hi():
    print("hi")

hi()