"""
Write a python function to check whether the given number is even or not.
assert is_Even(1) == False
"""
def is_Even(n):
    # Check if the number is divisible by 2 without a remainder
    return n % 2 == 0

# Test the function with the provided test case
assert is_Even(1) == False
