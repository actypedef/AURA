"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
def number_of_substrings(s):
    # Calculate the length of the string
    n = len(s)
    
    # Use the formula for the sum of the first n natural numbers to find the total number of substrings
    return int(n * (n + 1) / 2)

# Test the function with the provided test case
assert number_of_substrings("abc") == 6
