"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""
def upper_ctr(s):
    # Initialize counter for uppercase characters
    uppercase_count = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the character is uppercase
        if s[i] >= 'A' and s[i] <= 'Z':
            uppercase_count += 1
    
    return uppercase_count

# Test the function with the provided test case
assert upper_ctr('PYthon') == 1
