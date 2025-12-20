# Goal: creates a global variable x=10. Write a 
#       function change_x() that sets x = 20 inside it. print x outside the function.

x = 10

def chnage_x():
    x = 20

chnage_x()
print(x)

#Explanation:
# The variable x inside the function change_x() is a local variable.
# It does not affect the global variable x.
# So, the output outside the function remains 10.
# If we want to chnage the global x inside the function, we should use the global keyword.