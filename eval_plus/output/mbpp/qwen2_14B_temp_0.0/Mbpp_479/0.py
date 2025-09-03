"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
def first_Digit(n):
    # Loop until n is reduced to a single digit
    while n >= 10:
        n = n / 10
    # Convert n to an integer and return it
    return int(n)

# Test the function with the provided test case
assert first_Digit(123) == 1
