# Goal : Remove all negative numbers from a list using filter().
# Deep dive: filter (func, list) keeps items where func(items) returns Truthy. Passing 
#            None as the function automatically filters out Falsy values(0,"",None).

rmv = list(filter(lambda x:x>0, [0,-2,3,134,4]))

print(rmv)

print(list(filter(None,[-1,0,None,'hi',''])))