"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
def number_of_substrings(s):
    # Initialize the result variable to store the total number of substrings
    res = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # For each character, add the number of substrings starting from this character
        res += len(s) - i
    
    return res

# Test the function with the provided test case
assert number_of_substrings("abc") == 6
