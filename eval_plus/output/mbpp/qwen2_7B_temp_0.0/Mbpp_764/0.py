"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
def number_ctr(str):
    # Initialize counter for digits
    ctr = 0
    
    # Iterate through each character in the string
    for i in range(len(str)):
        # Check if the current character is a digit
        if str[i].isdigit():
            ctr += 1
    
    return ctr

# Test the function with the provided test case
assert number_ctr('program2bedone') == 1
