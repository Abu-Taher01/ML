# Goal: Create a list of 10 million numbers.
#       Check if -1 is in the list.
       
# Deep Dive: Python performs a Linear Search.
#            Time Complexity: O(n)

number = list(range(10000000))

def linear_scan():
    if -5 in number:
        print("Found")
    else:
        print("Not Found")

linear_scan()

# output: Not Found

number[100] = -5

linear_scan()

# output: Found 