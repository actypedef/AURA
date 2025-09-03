"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
def number_of_substrings(s):
    # Calculate the length of the string
    n = len(s)
    
    # Initialize count to store the number of non-empty substrings
    count = 0
    
    # Iterate over all possible starting points of substrings
    for i in range(n):
        # For each starting point, iterate over all possible ending points
        for j in range(i + 1, n + 1):
            # Increment the count for each valid substring
            count += 1
    
    return count

# Test the function with the provided test case
assert number_of_substrings("abc") == 6
