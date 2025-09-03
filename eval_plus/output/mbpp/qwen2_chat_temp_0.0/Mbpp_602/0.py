"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(s):
    # Create an empty dictionary to store characters and their indices
    char_dict = {}
    
    # Iterate over each character in the string along with its index
    for i, c in enumerate(s):
        # Check if the character is already in the dictionary
        if c in char_dict:
            # If it is, return the character as it's the first repeated one
            return c
        else:
            # If not, add the character to the dictionary with its index
            char_dict[c] = i
    
    # If no repeated character is found, return None
    return None

# Test the function with the provided test case
assert first_repeated_char("abcabc") == "a"
