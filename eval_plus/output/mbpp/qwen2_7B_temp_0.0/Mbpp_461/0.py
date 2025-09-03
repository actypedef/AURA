"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(str):
    # Initialize a counter for uppercase characters
    ctr = 0
    
    # Iterate through each character in the string
    for char in str:
        # Check if the character is an uppercase letter
        if char >= 'A' and char <= 'Z':
            ctr += 1
    
    # Return the total count of uppercase characters
    return ctr

# Test the function with the provided test case
assert upper_ctr('PYthon') == 1
