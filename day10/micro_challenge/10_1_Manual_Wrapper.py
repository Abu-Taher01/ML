# Goal: Write a function Wrapper(func) that runs code before/after func. Apply it manually: 
#       new_func = wrapper(old_func)

# Deep dive: This demystifics the @ syntax. A decorator is simply a function that takes a function and returns a function.

def wrapper(func):
    def inner():
        print("pre")
        func()
        print("Post")
    return inner

def hi():
    print("hi")

new_func = wrapper(hi)
new_func()