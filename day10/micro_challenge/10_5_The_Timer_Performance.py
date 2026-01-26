# Goal: Create a @timer decoorater that prints execution using time.time().

# Deep dive: This is AOP(As pect Oriented Programming). 
#            We inject timing logic into the function without modifing the function's actual code.

import time

def timing(func):
    def wrap(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("Executed time: ", start-end)
        return result
    return wrap


@timing
def add(a,b):
    return a+b

print(add(5,10))

