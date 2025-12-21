# Goal: Create a variable x=0. Try to print 100/x. Catch the specific error that occurs.

x = 0

try:
    result = 100/x
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")