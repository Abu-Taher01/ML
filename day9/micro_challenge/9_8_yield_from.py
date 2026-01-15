# Goal: Write a generator that yields values from two different sub-generators usig yield from.

# Deep dive: yield from delegates the generator operation to another sub-generator.
#            It flattens nested strutures efficiently without manual loops.

def gen():
    yield from [1,2,3]

for x in gen():
    print(x)

def inner():
    yield 1
    yield 2

def outer():
    yield 0
    # for _ in inner():
    #     yield _
    yield from inner()
    yield 3

for x in outer():
    print(x)


def gen1():
    yield from range(5)

print(list(gen1()))