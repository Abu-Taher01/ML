# Goal: Create two generators: one squares numbers, the other filters evens.
#       Chain them: filter(square(nums)).

# Deep dive: This creates a Data Pipeline. Data flows from source -> square -> filter.
#           NO intermidiate lists are created in RAM.

import time

start  = time.time()

def square():
    for n in range(10000):
        yield n*n

def filter(nums):
    for n in nums:
        if n%2==0:
            yield n

# nums = [x for x in range(10000)]

for nums in filter(square()):
    print(nums)

# g = filter(square())
# print(list(g))

end = time.time()

print("Execution Time:", end - start)