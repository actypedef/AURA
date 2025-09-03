"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""
def is_Diff(n):
    """
    This function checks if a number is divisible by 11.
    """
    return n % 11 == 0

# Test cases
assert is_Diff(12345) == False
assert is_Diff(121) == True
assert is_Diff(123456789) == False
assert is_Diff(1234567890) == True