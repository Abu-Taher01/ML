# Goal: Use gen.send(values) to inject data into running generator. 
# Deep dive: Generators can be two-way streets. 
#            val = yield pauses and waits to recive data from the outsides world.
#            This is the basis for Coroutines(AsyncIO)

def accumulator():
    total = 5
    while True:
        val = yield total
        total += val

acc= accumulator()
print(next(acc))
print(acc.send(10))
print(acc.send(5))

# Generators are usually producers (Output only).
# .send() turns them into Consumers. When the generator yields, it pauses.
# .send(val) resumes the generator, but it replaces the yield expression with
# val inside the generator’s local scope.