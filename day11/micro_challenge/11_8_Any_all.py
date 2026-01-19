# Goal: Check if any number in a list is negative. Check if all are positive. 
# Deep dive: These are short-circuiting operations. any() stops at the first True.
#            all() stops at the first False. This is O(1) in the best case.

ls = [2,1,4,-3,-5,3]

print(all(x>=0 for x in ls))

print(any(x>=0 for x in ls))

print(all(['hi','hello','']))

print(all(['hi','hello']))