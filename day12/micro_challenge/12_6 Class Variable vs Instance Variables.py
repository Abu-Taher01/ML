# Goal: Set species ="Human" on the class. Set name = "A" on the instance.
#       Change species and see who is affetced.
#
# Deep Dive: Class variables are shared by ALL instances(Memory Optimization).
#            Instance variables are unique to the object.

class Creature:
    species = "Human"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        # self.species = "Alien"  # Instance variable
        
person1 = Creature("A")
person1.species = "Alien"  # Changing instance variable

person2 = Creature("B")

print(person1.species)  # Output: Alien
print(person2.species)  # Output: Human

# instance is object.
# instance: an individual object of a class.
# object: a more general term that refers to any data structure in Python.
# In Python, all instances are objects, but not all objects are instances of a user-defined class.