# Goal: Create a list of 1 million numbers. Create a set (hash table) of the same numbers. 
#       Check if the number -1 exists in both.

number_list = [i-50000 for i in range(1000000)]
number_set = set(number_list)

print(-1 in number_list)
print(-1 in number_set)