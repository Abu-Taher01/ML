# Goal: Calculate the product of a list (1*2*3*4) using functools.reduce.
# Deep dive: reduce Collapses a list into a single value. 
#            It takes item 1 and 2, applies the function, takes the result and item 3, 
#            applies again...... until one item remains.

from functools import reduce

print(reduce(lambda a,b : a*b, [1,2,3,4,5]))

print(reduce(lambda a,b : a+b, [1,2,3,4,5]))

# finding max
print(reduce(lambda a,b: a if a>b else b, [1,2,7,5,6,4,10]))