"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(s):
    # Create an empty set to store characters we've seen
    char_set = set()
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is already in the set
        if char in char_set:
            return char  # Return the first repeated character
        else:
            char_set.add(char)  # Add the character to the set
    
    return None  # Return None if no character repeats

# Test the function with the provided test case
assert first_repeated_char("abcabc") == "a"