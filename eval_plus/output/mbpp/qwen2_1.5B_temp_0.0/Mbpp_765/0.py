"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n * 2

# Test cases
assert is_polite(7) == 11