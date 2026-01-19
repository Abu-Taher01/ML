# Goal: Combine name = ['A','B'] and ages = [20,30] into a dictionary. 
# Deep Dive: dict(zip(names,ages)).
#            Zip creates an iterator of tuples. 
#            dict() consumes those tuples to build the hash map.


name = ['A','B']
ages = [20,30]

dc = dict(zip(name,ages))

print(dc['A'])

for a,b in zip(['X','Y'],[10,20]): print(a,b)

print(list(zip([1,2,3],['a','b'])))