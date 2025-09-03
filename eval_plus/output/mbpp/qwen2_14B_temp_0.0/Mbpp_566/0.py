"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: return the last digit plus the sum of the remaining digits
        return n % 10 + sum_digits(int(n / 10))

# Test the function with the provided test case
assert sum_digits(345) == 12
