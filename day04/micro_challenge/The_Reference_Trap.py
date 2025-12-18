# Goal : Create a List a = [1,2,3]. Set b = a. 
#        Change the first item to 99. print a.

# Wrong way of copying a list in Python:
a = [1,2,3]
print(f'Initial a={a}')
# output: Initial a=[1, 2, 3]
b = a
b[0] = 99
print(f'a={a}, b={b}')
# output: a=[99, 2, 3] , b=[99, 2, 3]; here a chnaged because b is just a reference to a.

#Solution : 
# 1) list.copy()
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(f'a={a}, b={b}')
# output: a=[1, 2, 3], b=[99, 2, 3]

# 2) list slicing
c = a[:]
c[0] = 99
print(f'a={a}, c={c}')
# output: a=[1, 2, 3], c=[99, 2, 3]