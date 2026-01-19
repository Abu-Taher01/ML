# Goal: Try to modify a tuple inside a map function.
# Deep dive: Functional programming relies on **Immutability**.
#            Functions should not have side effects(modifying global state).
#            They should receive input and return new output.

t=(1,2,3)
try:
 t[0]=10
except TypeError as e:
 print(e)

