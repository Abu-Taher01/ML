# Wrong way of copying a list in Python:

a = [1,2,3]
print(f'Initial a={a}')
# output: Initial a=[1, 2, 3]

b = a

b[0] = 99

print(f'a={a}, b={b}')
# output: a=[99, 2, 3]

#Fix: 
# 1) list.copy()

c = a.copy()

c[0] = 23

print(f'a={a}, c={c}')
# output: a=[99, 2, 3], c=[23, 2, 3]

# 2) list slicing
d = a[:]

d[0] = 45

print(f'a={a}, d={d}')
# output: a=[99, 2, 3], d=[45, 2, 3]