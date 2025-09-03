"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
def last_Digit(n):
    # Return the last digit of the number n
    return n % 10

# Test the function with the provided test case
assert last_Digit(123) == 3
