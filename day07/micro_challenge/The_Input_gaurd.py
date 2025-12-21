# Goal : Write a program that ask the user for their age.
#        If they type text(e.g. "twenty"), print "Number only" instead of crashing.

# Constraint : Use try/except ValueError.

age = input("Please enter your age: ")

try:
    age_int = int(age)
    print(f"Your age is {age_int}.")
except ValueError:
    print("Number only")

# Explanation:
# We ask the user to input their age.
# We use a try block to convert the input to an integer.
# If the conversion is successful, we print the age.
# If a ValueError occurs (e.g., the user inputs text instead of a number),
# we catch the exception in the except block and print "Number only".