"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
def first_Digit(n):
    # Loop until n has only one digit
    while n >= 10:
        n = int(n / 10)
    return n

# Test the function with the provided test case
assert first_Digit(123) == 1
