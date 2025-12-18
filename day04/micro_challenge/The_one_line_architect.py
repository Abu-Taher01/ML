# Goal: Create a list of numbers from 1 to 10. Generate a new list
#       that containing the squares of only the even numbers.

numbers = list(range(1,11))
print(numbers)

# with list comprehension:
squared = [i**2 for i in numbers if i%2==0]

# without list comprehension:
# for i in numbers:
#     if i%2 == 0 :
#         squared.append(i**2)

print(squared)