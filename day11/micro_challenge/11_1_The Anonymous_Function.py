# Goal: Write a function using lambda. 
# Deep dive: Lambda creates a function object on the heap but assigns 
#            it no names(unless you bind it to a variable).it is purely
#            Syntactic sugar for single-expression functions.

# =================================================

add = lambda x,y : x+y

print(add(5,10))

# =================================================

print((lambda x: x*x)(5))

# =================================================

funcs = [lambda x=i: x*x for i in range(5)]

for f in funcs: 
    print(f())

