# Goal: Compare sys.getsize() of a list comprehension vs a generator expression 
#       for 1 million numbers.
 
# Deep dive: A list comprehension builds the entire list in memory,
#       while a generator expression produces items one at a time.
#       [x for x in range(1000000)] consumes ~8MB RAM(stores all numbers).
#       (x for x in range(1000000)) consumes ~112 bytes RAM (stores only the state/logic).

import sys

#list comprehension
listComp = [x for x in range(1000000)]

print(sys.getsizeof(listComp))

gen = (x for x in range(1000000))

print(sys.getsizeof(gen))

#how it works:
# The list comprehension creates a list containing all 1 million numbers.
# which requires memory to store all those numbers.
# The generator expression, on the other hand, only keeps track of the current state.
# so it uses significantly less memory.
# Thus, sys.getsizeof() shows a much larger size for the list comprehension.
# compared to the generator expression.