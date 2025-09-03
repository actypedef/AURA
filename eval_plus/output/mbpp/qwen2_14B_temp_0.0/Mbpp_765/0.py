"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
import math 

def is_polite(n): 
    # Increment n to account for 0-based indexing
    n = n + 1
    # Calculate the nth polite number using the given formula
    return int(n + (math.log((n + math.log(n, 2)), 2)))

# Test the function with the provided test case
assert is_polite(7) == 11
