# Goal: Compare list.append(x) vs list.insert(0,x).
# Deep dive: .append() puts data in the next empty memory slot(O(1)).
#            .insert(0,x) forces Python to shift every single existing item one step to the right in memory to make room.

number = list()

number.append(1)
number.append(2)

number.insert(0,5)

print(number)