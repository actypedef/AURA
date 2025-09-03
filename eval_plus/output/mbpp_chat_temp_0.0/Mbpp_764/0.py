"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
def number_ctr(str):
    # Initialize a counter for digits
    num = 0
    
    # Iterate through each character in the string
    for i in range(len(str)):
        # Check if the current character is a digit
        if str[i] >= '0' and str[i] <= '9':
            num += 1
    
    return num

# Test the function with the provided test case
assert number_ctr('program2bedone') == 1
