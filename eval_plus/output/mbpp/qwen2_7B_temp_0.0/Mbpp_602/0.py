"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(s):
    # Create an empty dictionary to store characters and their indices
    char_index = {}
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is already in the dictionary
        if char in char_index:
            # If found, return the character as it's the first repeated one
            return char
        else:
            # Otherwise, add the character to the dictionary with its index
            char_index[char] = i
    
    # If no repeated character is found, return None
    return None

# Test the function with the provided test case
assert first_repeated_char("abcabc") == "a"
