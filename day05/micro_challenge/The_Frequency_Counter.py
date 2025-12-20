# Goal: Input a string "banana". 
#       Create a dictionary counter that counts the frequency of each letter (e.g., {'b': 1, 'a': 3, 'n': 2}).

str = "banana"
dict = {}

for letter in str:
    if letter in dict:
        dict[letter] +=1 
    else :
        dict[letter] = 1

print(dict)

# Explanation:
# We initialize an empty dictionary 'dict' to store the frequency of each letter.
# We iterate through each letter in the input string 'str'.
# If the letter is already a key in the dictionary, we increment its value by 1.
# If the letter is not in the dictionary, we add it with an initial value of 1.
# Finally, we print the dictionary containing the frequency of each letter.