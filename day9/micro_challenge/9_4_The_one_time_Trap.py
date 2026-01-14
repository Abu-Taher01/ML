# Goal: Create a generator g. Lop through it once. Try to loop through it again.

# Deep dive: Generators are Exhaustible. Once iterated, the 'cursor is at the end.
#            You cannot rewind a generator; you must re-instantiate it.

def g():
    for i in range(7):
        yield i

gen = g()

for _ in range(6):
    print(next(gen))

gd = g()

print(list(gd))
print(list(gd))