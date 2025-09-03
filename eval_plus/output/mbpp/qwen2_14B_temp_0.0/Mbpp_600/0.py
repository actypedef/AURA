"""
Write a python function to check whether the given number is even or not.
assert is_Even(1) == False
"""
def is_Even(n):
    # Check if the number is divisible by 2
    return n % 2 == 0

# Test cases
assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(0) == True
assert is_Even(-4) == True
assert is_Even(-3) == False
