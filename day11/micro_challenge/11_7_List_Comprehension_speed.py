# Goal: Compare map(lambda...) vs [X... for X...] 
# Deep dice: List Comprehensions are generally faster than map+lambda becuase they avoid the 
#            overhead of alling a python function frame for evey single item.

import time

start =time.time()
ls_comprehension = [x*x for x in range(500000)]
end = time.time()

print(end-start)

start =time.time()
mp_lambda = list(map(lambda x : x*x, range(500000)))
end = time.time()

print(end-start)

print([x for x in range(10) if x%2==0])

