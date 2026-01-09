# Goal: Write a function gen(n) that yields 1, then 2, then 3.loop through it.

# Deep dive: Unlike return, yield pauses the function and saves the 
#            Stake Frame(local Varibales) in RAM.
#            The function is frozen util you call it again.


def gen(n):
    for i in range(1,n+1):
        yield i

g = gen(10)

print('with next', next(g))

for i in g:
    print(i)