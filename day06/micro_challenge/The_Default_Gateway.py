# Goal: Write a function connect(port=3306) that prints "Connect to [ports]". 
#       Call it once with no arguments and once with port=5432.

def connect(port=3306):
    print(f"Connect to [{port}]")

connect()

connect(port=5432)

# Explanation:
# This uses default arguments in function defination in Python.
# When connect() is called without arguments, it uses the default port 3306.
# When connect(port=5432) is called, it overrides the default with 5432
# This is useful for setting optional common default values while allowing flexibility.