# Goal: Create a decorator that accepts a setting: @ repeat(times=3).
# Deep dive: This requires Three Level of nested Functions
#            1. The factory(accepts 'times').
#            2. The decorator (accepts 'func').
#            3. Th Wrapper(accepts 'args'). 


def repeat(times):
    def deco(func):
        def wrap():
            for _ in range(times):
                print(func())
            # return func()
        return wrap
    return deco

@repeat(3)
def greet():
    return f"Greet the world!"

greet()