# Goal: Write a try/except that divides two numbers. Add finally block that 
#       prints "Execution Complete" regardless of whether an error succeeds or failed.

try:
    num1 = float(input("Enter the numerator:"))
    num2 = float(input("Enter the denominator:"))
    result = num1 / num2
    print(f"Result : {result}")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Execution Complete")

# Explanation:
# We use a try block to divide two numbers input by the user.
# If the user tries to divide by zero, a ZeroDivisionError is raised,
# which we catch in the except block and print an error message.
# The finally block is executed regardless of whether an error occurred or not.