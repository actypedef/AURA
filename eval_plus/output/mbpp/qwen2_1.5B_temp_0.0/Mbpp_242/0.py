"""
Write a function to count the total number of characters in a string.
assert count_charac("python programming")==18
"""
def count_charac(s):
    return len(s)

# Test cases
assert count_charac("python programming") == 18
assert count_charac("hello world") == 11
assert count_charac("") == 0
assert count_charac("a") == 1