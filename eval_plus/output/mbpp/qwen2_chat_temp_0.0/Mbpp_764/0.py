"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
def number_ctr(s):
    # Initialize a counter for digits
    ctr = 0
    
    # Iterate through each character in the string
    for i in s:
        # Check if the character is a digit
        if i.isdigit():
            ctr += 1
            
    return ctr

# Test the function with the provided test case
assert number_ctr('program2bedone') == 1