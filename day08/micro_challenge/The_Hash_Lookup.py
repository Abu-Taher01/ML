# Goal: Convert that list to a set.
#       Check for -5 again.

# Deep Dive: Python runs hash(-5).
#            gets a memory address, and look up directly
#            at that slot. It never scans the other items.
#            complexity: O(1) 

number = list(range(10000000))
number_set = set(number)

def hash_lookup():
    if -5 in number_set:
        print("Found")
    else:
        print("Not Found")

hash_lookup()  
# output: Not Found

number_set.add(-5)

hash_lookup()
# output: Found