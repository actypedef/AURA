"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
def number_of_substrings(s):
    # Calculate the length of the string
    n = len(s)
    
    # Initialize the result variable to store the total number of substrings
    res = 0
    
    # Loop through each character in the string
    for i in range(n):
        # For each character, add the number of possible substrings starting from that character
        res += (n - i)
    
    # Return the total number of non-empty substrings
    return res

# Test the function with the provided test case
assert number_of_substrings("abc") == 6
