# Goal: Sort ["100px", "20px", "3px"] numerically (so 3px comes first). 
# Deep Dive: sorted(data, key = lambda x: int (x[:-2])). The key function transforms the 
#            item only for comparison purposes, leaving the original data intact.

data = ['100px','20px','3px']
y = sorted(data, key = lambda x: int(x[:-2]))

print(y)

print(sorted([(1,3),(2,1),(0,2)],key=lambda x:x[1]))

# it works kind of like c++ sort comparator function 