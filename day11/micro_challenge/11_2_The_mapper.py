# Goal: Square a list of numbers using map(). 
# Deep Dive: map(func,list) pushes the loop into C-speed.
#           It returns an iterator(lazy), not a list. You must cast it with list()
#           to trigger execution.

square = list(map(lambda x:x*x,[1,2,3,4,5]))

print(square)

# ==========================================================


print(list(map(len,['apple','banana'])))


# ==========================================================

print(list(map(lambda a,b:a+b, [1,2], [2,3])))