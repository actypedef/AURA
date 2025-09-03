"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""
def number_of_substrings(s):
    # Initialize the count of substrings
    count = 0
    
    # Iterate over all possible starting points of substrings
    for i in range(len(s)):
        # Iterate over all possible ending points of substrings starting from i
        for j in range(i + 1, len(s) + 1):
            # Increment the count for each valid substring
            count += 1
            
    return count

# Test cases to verify the correctness of the function
assert number_of_substrings("abc") == 6
assert number_of_substrings("") == 0
assert number_of_substrings("a") == 1
assert number_of_substrings("aa") == 3
assert number_of_substrings("abcd") == 10