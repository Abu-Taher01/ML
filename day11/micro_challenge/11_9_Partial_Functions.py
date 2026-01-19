# Goal: Create a function power(base, exp). USe functools.partial to 
#       create a new function square(x) that locks exp=2. 

# Deep dive: Partials "freeze" argumets. This is useful when you need to pass a function to a
#            callback(like in UI frameworks) that expects fewer arguments.

from functools import partial
def power(base, exp):
    return base**exp

square = partial(power,exp=2)

print(square(5))