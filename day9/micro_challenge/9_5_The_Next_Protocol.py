# Goal: Manually call next(gen) until it crashes. 
# Deep dive: When a generator runs out of items, it raises StopIteration exception.
#            for loops catch this exception silently to stop iteration.

def g():
    for i in range(3):
        yield i

gen = g()

for i in range(5):
    try:
        print(next(gen))
    
    except StopIteration:
        print("Generator Exhausted!")

# for _ in range(2):
#     try:
#         print(list(gen))
    
#     except StopIteration:
#         print("Generator Exhausted!")